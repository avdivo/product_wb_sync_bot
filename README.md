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

## Структура проекта

```
/product_wb_sync_bot
├── alembic                   # Директория для миграций базы данных Alembic
│   ├── versions              # Папка с файлами миграций
│   ├── env.py                # Основной файл конфигурации Alembic
│   ├── README                # Описание для Alembic
│   └── script.py.mako        # Шаблон для генерации миграций
├── api                       # Директория с логикой API
│   ├── __init__.py           # Инициализация модуля API
│   ├── endpoints.py          # Эндпоинты приложения
│   └── services.py           # Логика бизнес-процессов для API
├── bot                       # Логика Telegram-бота
│   ├── __init__.py           # Инициализация модуля бота
│   ├── handlers.py           # Хэндлеры событий бота
│   └── states.py             # Управление состояниями бота
├── config                    # Конфигурационные модули проекта
│   ├── __init__.py           # Инициализация модуля конфигураций
│   ├── app.py                # Конфигурация приложения FastAPI
│   ├── config_bot.py         # Конфигурация Telegram-бота
│   ├── config_db.py          # Конфигурация базы данных
│   └── config_scheduler.py   # Конфигурация планировщика задач
├── db                        # Работа с базой данных
│   ├── __init__.py           # Инициализация модуля базы данных
│   ├── crud.py               # CRUD-операции для моделей
│   └── models.py             # Определение моделей базы данных
├── schemas                   # Схемы данных
│   ├── __init__.py           # Инициализация модуля схем
│   └── schemas.py            # Pydantic-схемы для валидации данных
├── scripts                   # Сторонние скрипты
│   └── wait-for-it.sh        # Скрипт ожидания запуска сервисов
├── venv                      # Виртуальное окружение Python
├── .env                      # Файл конфигурации окружения (локальный)
├── .env_server               # Файл конфигурации окружения (для сервера)
├── alembic.ini               # Конфигурация Alembic
├── docker-compose.yml        # Конфигурация Docker Compose
├── Dockerfile                # Dockerfile для сборки контейнера
├── main.py                   # Точка входа в приложение
├── README.md                 # Файл с описанием проекта
└── requirements.txt          # Файл зависимостей Python
```

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
APP_PORTS=8000:8000 <Внешний и внутренний порты контейнера. Без контейнера запускается на внутреннем>

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
