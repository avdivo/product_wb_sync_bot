import httpx
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import ValidationError

from schemas.schemas import Response
from db.crud import create_or_update_product
from config.config_db import async_session


async def fetch_product_details(db: AsyncSession,  article_number):
    """Делает запроc товара к WB по его артикулу

    :param article_number:
    :return: json
    """
    print(article_number, type(article_number), '-----------------------------')
    url = f"https://card.wb.ru/cards/v1/detail"
    params = {
        "appType": 1,
        "curr": "rub",
        "dest": -1257786,
        "spp": 30,
        "nm": article_number
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()  # Проверка на ошибки HTTP

    try:
        # Десериализация JSON с использованием Pydantic
        response_data = Response.parse_raw(response.text)
    except ValidationError as e:
        raise HTTPException(
            status_code=502,
            detail={
                "error": "Invalid response structure from upstream service",
                "details": e.errors(),
            },
        )

    if not response_data.data.products:
        raise HTTPException(status_code=404, detail="Product not found")

    # Извлечение нужных данных из разобранного объекта
    product = response_data.data.products[0]

    article = product.id
    name = product.name
    price = product.salePriceU / 100 if product.salePriceU else 0  # Переводим в рубли
    rating = product.rating
    total_quantity = product.totalQuantity

    product = await create_or_update_product(db, article, name, price, rating, total_quantity)

    return product


async def update_product_by_article(article: str):
    """Логика обновления информации о товаре."""
    # Создаем новую сессию вручную
    async with async_session() as session:
        await fetch_product_details(session, article)
