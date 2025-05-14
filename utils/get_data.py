import os
import sys
import redis
import yaml
import logging
from dotenv import load_dotenv

# Добавляем корневой каталог проекта в PYTHONPATH для удобства импорта
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_PATH)

# Загружаем переменные окружения из файла .env
dotenv_path = os.path.join(PROJECT_PATH, ".env")  # Путь к файлу .env
load_dotenv(dotenv_path, override=True)  # Загружает переменные окружения из .env в os.environ

CONFIG_FILE_PATH = os.path.join(PROJECT_PATH, "src", "config.yaml")

logging.basicConfig(level=logging.INFO)


def get_bot_token() -> str:
    """
    Получает токен бота из переменной окружения TELEGRAM_BOT_TOKEN.

    Returns:
        str: Токен бота.
    """
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        logging.error("Ошибка: Переменная окружения TELEGRAM_BOT_TOKEN не задана.")
        return None  # Или raise EnvironmentError

    return token


def update_config_file(token: str=None, redis_host: str=None, redis_port: int=None, redis_db: str=None):
    """
    Обновляет config.yaml с токеном бота и/или параметрами базы данных.

    Args:
        token (str): Токен бота.
        redis_host (str, optional): Хост базы данных. Defaults to None.
        redis_port (int, optional): Порт базы данных. Defaults to None.
        redis_db (str, optional): Имя базы данных. Defaults to None.
    """
    config_data = {"bot_token": token}

    if redis_host is not None:  # Проверяем, что host передан
        config_data["host"] = redis_host
        config_data["port"] = redis_port
        config_data["database"] = redis_db

    try:
        with open(CONFIG_FILE_PATH, "w") as file:
            yaml.dump(config_data, file)
    except Exception as e:
        logging.error(f"Ошибка при записи в config.yaml: {e}")


def get_redis_connection_params() -> list[str]:
    """
    Извлекает параметры подключения к базе данных из файла конфигурации.

    Returns:
        list[str]: Список параметров подключения [host, port, database].
    """
    try:
        with open(CONFIG_FILE_PATH, "r") as file:
            config = yaml.safe_load(file)
            host = os.environ.get("REDIS_HOST") or config.get("redis_host")
            port = os.environ.get("REDIS_PORT") or config.get("redis_port")
            database = os.environ.get("REDIS_DB") or config.get("redis_db")

            return [host, port, database]
    except FileNotFoundError:
        print(f"Ошибка: Файл конфигурации не найден: {CONFIG_FILE_PATH}")
        return []
    except KeyError as e:
        print(f"Ошибка: Ключ '{e}' отсутствует в файле конфигурации.")
        return []
    except yaml.YAMLError as e:
        print(f"Ошибка: Ошибка при чтении YAML файла: {e}")
        return []


def redis_conn(redis_host: str, redis_port: int, redis_db: int) -> redis.Redis:
    """
    Создает и проверяет подключение к Redis.

    Устанавливает соединение с сервером Redis, используя предоставленные параметры хоста,
    порта и базы данных, и выполняет ping для проверки соединения.

    Args:
        redis_host: Хост Redis (например, "localhost").
        redis_port: Порт Redis (обычно 6379).
        redis_db: Индекс базы данных Redis (обычно 0).

    Returns:
        Объект Redis (redis.Redis) для дальнейшего взаимодействия с Redis.
        В случае ошибки подключения, функция завершает выполнение программы (exit())."""
    
    redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

    try:
        redis_client.ping()
        print("Успешно подключено к Redis!")

    except redis.exceptions.ConnectionError as e:
        print(f"Ошибка подключения к Redis: {e}")
        exit()

    return redis_client