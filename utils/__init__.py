
"""
Этот модуль инициализирует пакет, импортируя функции для получения данных конфигурации:

- `get_bot_token`: Функция для получения токена бота.
- `get_admins_ids`: Функция для получения списка ID администраторов.
- `get_db_connection_params`: Функция для получения параметров подключения к базе данных.
"""

from utils.get_data import get_bot_token, get_redis_connection_params, update_config_file, redis_conn

