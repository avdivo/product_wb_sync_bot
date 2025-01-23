import asyncio
from fastapi import APIRouter, Request, Depends, Path
from fastapi.responses import JSONResponse
from aiogram.types import Update
from sqlalchemy.ext.asyncio import AsyncSession

from config.config import Config
from config.config_bot import bot, dp
from config.config_db import get_db
from schemas.schemas import ProductRequest, ProductOut, SubscriptionResponse, SubscribePath
from .services import fetch_product_details, update_product_by_article
from config.config_scheduler import scheduler


api_router = APIRouter(prefix="/api/v1")
webhook_router = APIRouter()


@webhook_router.post(Config.WEBHOOK_PATH, include_in_schema=False)
async def handle_webhook(request: Request, db: AsyncSession = Depends(get_db)):
    """Обработка запросов. Передача боту.
    """
    update_data = await request.json()  # Получение данных из запроса
    update = Update(**update_data)  # Создание объекта обновления
    asyncio.create_task(dp.feed_update(bot, update, db=db))  # Передача обновления боту
    return JSONResponse(content={})  # Возвращение пустого ответа


@api_router.post("/products", response_model=ProductOut)
async def get_items(request: ProductRequest, db: AsyncSession = Depends(get_db)):
    return await fetch_product_details(db, request.article)


@api_router.get(
    "/subscribe/{artikul}",
    summary="Подпишитесь на обновления продукта",
    description="Включает периодическое обновление информации для указанного артикула.",
    response_model=SubscriptionResponse,
    response_description="Успешное подключение к обновлениям для товара."
)
async def subscribe_to_product(artikul: SubscribePath = Depends()):
    """Включение обновления для конкретного артикула.
       - **artikul**: Артикул товара.
    """
    job_id = f"update_{artikul}"

    # Добавляем новую задачу для обновления товара
    scheduler.add_job(
        update_product_by_article,
        trigger="interval",
        # minutes=30,
        seconds=10,
        args=[artikul.artikul],
        id=job_id,
        jobstore='default',
        replace_existing=True
    )

    return SubscriptionResponse(detail=f"Включено периодичное обновление товара {artikul}")

