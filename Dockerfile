# Базовый образ python 
FROM python:3.12

# устанавливаем рабочую директорию 
WORKDIR /app

# копируем файл с зависимостями 
COPY requirements.txt .

# устнанавливаем зависимости 
RUN pip install --no cache-dir -r requirements.txt

# копируем в контейнер 
COPY . .

# устнавливаем переменную окружения
ENV PYTHONUNBUFFERED=1

# компанда для запуска скрипта
CMD ["python", "run_spider.py"]

