FROM python:3.11-slim

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование wait-for-it.sh в контейнер
COPY scripts/wait-for-it.sh /usr/local/bin/wait-for-it
RUN chmod +x /usr/local/bin/wait-for-it

# Копирование кода приложения
COPY . .

# Команда для выполнения миграций и запуска приложения
CMD alembic upgrade head && python main.py
