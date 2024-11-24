# Используем базовый образ Python
FROM python:3.12-slim

# Устанавливаем зависимости
WORKDIR /app

RUN pip install psycopg2-binary

# Копируем код приложения
COPY app_it2.py .

# Запускаем приложение
CMD ["python", "app_it2.py"]
