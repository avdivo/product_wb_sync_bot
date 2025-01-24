import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.asyncio import AsyncIOExecutor

from config.config import Config

DATABASE_URL = (f"postgresql+psycopg2://{Config.DB_USER}:{Config.DB_PASSWORD}"
                f"@{os.getenv('DB_HOST', 'localhost')}:5432/{Config.DB_NAME}")

# Создание хранилища задач APScheduler
jobstores = {
    'default': SQLAlchemyJobStore(url=DATABASE_URL)
}

executors = {
    'default': AsyncIOExecutor()
}

scheduler = AsyncIOScheduler(jobstores=jobstores, executors=executors)
