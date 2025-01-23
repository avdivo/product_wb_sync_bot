from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import ProductDB


async def create_or_update_product(db: AsyncSession, article: int, name: str, price: int, rating: float,
                                   total_quantity: int):
    """
    Создание или обновление товара
    """
    async with db.begin():
        # Проверка на существование товара с таким артикулом
        stmt = select(ProductDB).filter(ProductDB.article == article)
        result = await db.execute(stmt)
        product = result.scalar_one_or_none()

        if product:
            # Если товар существует, обновляем его данные
            product.name = name
            product.price = price
            product.rating = rating
            product.total_quantity = total_quantity
        else:
            # Если товара нет, создаем новый объект
            product = ProductDB(article=article, name=name, price=price, rating=rating,
                                total_quantity=total_quantity)
            db.add(product)  # Добавляем объект в сессию для сохранения

        await db.commit()
        return product


async def get_product_by_article(db: AsyncSession, article: int) -> ProductDB:
    """
    Получение товара по артикулу
    """
    async with db.begin():
        stmt = select(ProductDB).filter(ProductDB.article == article)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()


async def get_all_products(db: AsyncSession):
    """
    Получение всех товаров
    """
    async with db.begin():
        stmt = select(ProductDB)
        result = await db.execute(stmt)
        return result.scalars().all()
