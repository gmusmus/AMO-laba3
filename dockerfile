# Используйте официальный образ Python
FROM python:3.10

# Устанавливаем необходимые зависимости
RUN pip install numpy scikit-learn pandas

# Создаем директорию приложения в контейнере
RUN mkdir /app

# Копируем ваш Python-скрипт в контейнер
COPY main.py /app/main.py

# Устанавливаем рабочую директорию
WORKDIR /app

# Команда для выполнения вашего скрипта при запуске контейнера
CMD ["python", "main.py"]


