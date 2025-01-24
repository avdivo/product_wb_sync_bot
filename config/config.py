import os
from dotenv import load_dotenv
from fastapi.security import HTTPBearer

load_dotenv()


class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
    WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')
    WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALGORITHM = os.getenv('ALGORITHM')

    # Создание экземпляра HTTPBearer
    security = HTTPBearer()
