import asyncio
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from aiogram.types import Update
from sqlalchemy.ext.asyncio import AsyncSession

from config.config import Config
from config.config_bot import bot, dp
from config.config_db import get_db
from schemas.schemas import ProductRequest, ProductOut
from .services import fetch_product_details


api_router = APIRouter(prefix="/api/v1")
webhook_router = APIRouter()


@webhook_router.post(Config.WEBHOOK_PATH)
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


@api_router.get("/subscribe")
async def get_status():
    return {"status": "OK"}
