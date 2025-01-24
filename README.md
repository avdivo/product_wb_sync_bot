# ProductWBsyncBot


[**Swagger**](https://328c22e35a29.vps.myjino.ru/docs): https://328c22e35a29.vps.myjino.ru/docs  
[Телеграмм бот](https://t.me/ProductWBsync_bot): https://t.me/ProductWBsync_bot  
[GitHub](https://github.com/avdivo/product_wb_sync_bot): https://github.com/avdivo/product_wb_sync_bot


## Описание
Сервис для синхронизации товаров на Wildberries c БД

## Функции
- Синхронизация товара по артикулу (POST /api/v1/products)
- Добавление товара на автоматическую синхронизацию каждый 30 минут (GET /api/v1//subscribe/{article})
- Телеграм бот [WBsync](https://t.me/ProductWBsync_bot) для получения актуальной информации о товаре по артикулу
- Авторизация по JWT токену

## Используемые технологии
- Python 3.11
- PostgreSQL
- Alembic
- SQLAlchemy
- Pydantic
- FastAPI
- aiogram
- APScheduler
- docker, docker compose

## Файл .env
BOT_TOKEN=<Токен телеграм бота>  
WEBHOOK_HOST=<Домен>  
WEBHOOK_PATH=/webhook  
DB_NAME=<Имя БД>  
DB_USER=<Пользователь БД>  
DB_PASSWORD=<Пароль БД>  
SECRET_KEY=<Ключ, для валидации токена авторизации>  
ALGORITHM=<Протокол шифрования ключа>

## Установка и запуск в Docker контейнере
1. Открыть терминал.
2. Перейти в папку, где будет проект.
3. Клонировать репозиторий:
    ```bash
    git clone https://github.com/avdivo/product_wb_sync_bot
    ```
4. Войти в папку проекта.
    ```bash
    cd product_wb_sync_bot
    ```
5. Запустить проект в контейнере
    ```bash
    docker compose up --build
    ```

- Автоматически запустится контейнер с БД
- Создастся БД
- Создадутся таблицы
- Запустится приложение
