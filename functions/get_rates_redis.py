import os
import sys

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)

from config import REDIS_CONN
from functions import get_currency_rates_from_api


async def get_currency_rate(currency_pair: str) -> str | None:
    """
    Получает курс валюты из Redis, если он там есть.
    Иначе получает из API, сохраняет в Redis и возвращает.

    Args:
        currency_pair: (str) - пара валют, разделенных '_'.
                        Например: 'USD_EUR'.

    Returns:
        Курс валюты (str) из Redis или от API, или None, в случае ошибки.
    """
    rate = REDIS_CONN.get(currency_pair)

    if rate:
        print(f"Курс {currency_pair} получен из Redis")
        return rate.decode('utf-8')  # Преобразуем bytes в строку
    else:
        print(f"Курс {currency_pair} не найден в Redis. Получаем из API...")
        rates = await get_currency_rates_from_api([currency_pair])  # Получаем только нужную пару

        if currency_pair in rates:
            rate = str(rates[currency_pair])  # Преобразование в строку для Redis
            REDIS_CONN.setex(currency_pair, 17700, rate) # 2 часа 55 минут = 17700 секунд
            print(f"Курс {currency_pair} сохранен в Redis")
            return rate
        else:
            print(f"Ошибка: не удалось получить курс {currency_pair} из API.")
            return None