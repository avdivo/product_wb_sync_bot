from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Float
from config.config_db import Base


class ProductDB(Base):
    __tablename__ = "products"

    article = mapped_column(Integer, primary_key=True, index=True)  # Артикул товара (id)
    name = mapped_column(String, nullable=False)  # Название товара
    price = mapped_column(Integer, nullable=False)  # Цена товара в копейках
    rating = mapped_column(Float, nullable=False)  # Рейтинг товара
    total_quantity = mapped_column(Integer, nullable=False)  # Суммарное количество
