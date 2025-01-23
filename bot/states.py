from aiogram.fsm.state import State, StatesGroup


class ProductState(StatesGroup):
    """Состояния пользователя
    """
    enter_article = State()  # Ожидание артикула
