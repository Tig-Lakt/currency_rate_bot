"""
Модуль config.constants

Содержит константы и настройки, используемые в проекте, такие как токен бота,
пути к файлам с данными, параметры подключения к БД.
"""

import os
import sys
from utils import get_bot_token, get_redis_connection_params, update_config_file, redis_conn


update_config_file()

# Получаем абсолютный путь к корневой директории проекта.
# Используем os.path.dirname(__file__) для получения пути к текущему файлу (constants.py),
# затем переходим на один уровень выше, чтобы получить путь к PROJECT_PATH.
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Добавляем путь к проекту в sys.path, чтобы можно было импортировать модули из проекта.
sys.path.insert(0, PROJECT_PATH)

# Получаем токен бота из переменной окружения или файла конфигурации (см. utils.py).
TOKEN = get_bot_token()

# Получаем данные подключения к базе данных из переменной окружения или файла конфигурации (см. utils.py).
DB_CONN = get_redis_connection_params()

# Создание соединения с Redis.
REDIS_CONN = redis_conn(DB_CONN[0], DB_CONN[1], DB_CONN[2])

DATA_DIR = os.path.join(PROJECT_PATH, "data", "json") # Создаем переменную для пути к директории с данными
CURRENSIES_FILE = os.path.join(DATA_DIR, "currencies.json") # Путь к файлу, содержащему наименования валют и их коды 

# Список популярных валютных пар
CURRENCY_PAIRS = ['USD_RUB', 'RUB_EUR', 'EUR_USD', 'USD_KZT', 'EUR_KZT']