from flask import Flask

# создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)  # Создание экземпляра приложения Flask с указанием имени модуля (__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess' # Установка секретного ключа для защиты данных приложения

# Импорт модуля routes из пакета app для обработки маршрутов
from app import routes