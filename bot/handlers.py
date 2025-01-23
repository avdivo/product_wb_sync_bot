from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from sqlalchemy.ext.asyncio import AsyncSession

from db.crud import get_product_by_article
from .states import ProductState


async def show_main_menu(message: types.Message):
    """Отображение главного меню
    :param message:
    :return:
    """
    # Создание клавиатуры
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Получить данные по товару"),
            ],
        ],
        resize_keyboard=True
    )

    await message.reply("Нажмите кнопку, чтобы ввести артикул товара.", reply_markup=keyboard)


async def handle_product_article(message: types.Message, db: AsyncSession):
    """Прием артикула и вывод информации о товаре
    :param message:
    :param db:
    :return:
    """
    article = message.text
    try:
        product = await get_product_by_article(db, int(article))
    except ValueError:
        await message.answer(f"Ошибочный артикул.")
        return

    if product:
        out = f"""
Артикул: {product.article}
Товар: {product.name}
Цена: {product.price}
Рейтинг: {product.rating}
Количество на складах: {product.total_quantity}
        """
    else:
        out = 'Товар с таким артикулом не найден.'

    await message.answer(out)


async def handle_main_menu(message: types.Message, state: FSMContext):
    """Обработка нажатий на кнопки главного меню
    :param message:
    :param state:
    :return
    """
    await state.set_state(ProductState.enter_article)  # Устанавливаем состояние
    await message.answer("Введите артикул товара:")


async def start_command(message: types.Message):
    """Обработка команды /start"""
    await show_main_menu(message)  # Отображение главного меню


async def help_command(message: types.Message):
    """Обработка команды /help"""
    help_text = f"""
Бот позволяет получить данные о товаре по его артикулу в системе WB.

Доступные команды:
/start - Начать работу с ботом.
/help - Показать справку.

Кнопка "Получить данные по товару":
после нажатия кнопки нужно ввести артикул товара, чтобы получить информацию о нем..
    """
    await message.answer(help_text)


def register_handlers(router):
    """Регистрация обработчиков сообщений
    :param router:
    :return:
    """
    router.message.register(start_command, Command(commands=['start']))
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(handle_main_menu, F.text.in_(["Получить данные по товару"]))
    router.message.register(handle_product_article, StateFilter(ProductState.enter_article))
