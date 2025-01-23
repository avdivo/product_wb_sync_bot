from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List


class ProductRequest(BaseModel):
    """
    Проверка правильности передачи артикула
    """
    article: int = Field(..., description="Артикул товара", example=211695539)


# Ответ от WB
class Product(BaseModel):
    id: int  # Артикул товара
    name: str  # Название товара
    salePriceU: int  # Цена товара в копейках
    rating: float  # Рейтинг товара
    totalQuantity: int  # Суммарное количество товара на складах


class ResponseData(BaseModel):
    products: List[Product]


class Response(BaseModel):
    state: int  # Статус ответа
    params: dict  # Параметры запроса
    data: ResponseData

class ProductOut(BaseModel):
    article: int  # Артикул товара
    name: str  # Название товара
    price: int  # Цена товара в копейках
    rating: float  # Рейтинг товара
    total_quantity: int  # Суммарное количество товара на складах

    class Config:
        orm_mode = True


class SubscribePath(BaseModel):
    article: int = Field(..., title="Артикул товара", description="Уникальный номер товара.")


class SubscriptionResponse(BaseModel):
    detail: str
