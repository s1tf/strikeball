import os
import sys
import json
import flask

# Инициализируем Фласк
app = flask.Flask(__name__)

# Находим путь до приложения
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

# Загружаем конфиг
with open(os.path.join(application_path, 'config.json')) as f:
    config = json.load(f)


@app.route('/')
def main():
    """ Информация о сервере """
    return 'Сервер работает. Версия 0.1'


@app.route('/login/<password>')
def login(password):
    """ Проверка пароля"""

    # 1. Проверяем пароль в конфиге
    result = config['passwords'].get(password)

    # 2. Если пароль найден, возвращаем его Роль
    if result:
        return flask.jsonify({'role': result}), 200

    # 3. Если пароль не найден, возвращаем ошибку
    return flask.jsonify({'error': 'Неправильный пароль!'}), 401


# Запускаем Фласк
app.run()
