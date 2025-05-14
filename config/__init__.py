"""
Пакет config.

Содержит константы и настройки, необходимые для работы бота.

Экспортируемые переменные:
    TOKEN (str): Токен Telegram-бота.
    PROJECT_PATH (str): Путь к корневой директории проекта.
    DB_CONN (list): Данные для подключения к Redis.
    CURRENSIES_FILE (dict): Json-файл, содержащий названия валют и их коды.
    REDIS_CONN: Соединение с Redis.
    CURRENCY_PAIRS (list): Список популярных валютных пар.
"""

from config.constants import TOKEN
from config.constants import PROJECT_PATH
from config.constants import DB_CONN
from config.constants import CURRENSIES_FILE
from config.constants import REDIS_CONN
from config.constants import CURRENCY_PAIRS
