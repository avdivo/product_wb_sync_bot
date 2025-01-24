import logging
from fastapi import FastAPI

from api.endpoints import api_router, webhook_router
from .config import Config
from .config_db import create_tables
from .config_bot import bot, dp
from .config_scheduler import scheduler

app = FastAPI(title="ProductWBsyncBot")
app.include_router(api_router)  # Подключение маршрутов
app.include_router(webhook_router)  # Подключение маршрутов

logging.basicConfig(level=logging.INFO)  # Лог файл не создается, логи выводятся в консоль


# События
@app.on_event("startup")
async def on_startup():
    """Установка вебхука телеграмм, запуск планировщика,
    создание таблиц"""

    # Запускаем APScheduler
    scheduler.start()
    logging.info("APScheduler запущен")

    # Установка вебхука
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != Config.WEBHOOK_URL:
        await bot.set_webhook(Config.WEBHOOK_URL)
    logging.info(f"Webhook set to URL: {Config.WEBHOOK_URL}")

    # Создание таблиц в БД
    await create_tables()


@app.on_event("shutdown")
async def on_shutdown():
    """Удаление вебхука и закрытие хранилища при завершении работы приложения"""
    await bot.delete_webhook()
    await dp.storage.close()

    scheduler.shutdown()  # Останавливаем APScheduler
    logging.info("APScheduler остановлен")
