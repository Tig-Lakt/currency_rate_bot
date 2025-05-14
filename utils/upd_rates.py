import os
import sys

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)

from config import REDIS_CONN, CURRENCY_PAIRS
from functions import get_currency_rates_from_api


async def update_currency_rates_in_redis():
    """
    Обновляет курсы валют в Redis, получая их из API.
    """
    print("Обновляем курсы валют в Redis...")
    rates = await get_currency_rates_from_api(CURRENCY_PAIRS)
    for pair, rate in rates.items():
        REDIS_CONN.setex(pair, 17700, str(rate))
    print("Курсы валют в Redis обновлены.")