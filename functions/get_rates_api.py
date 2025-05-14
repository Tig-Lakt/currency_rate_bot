import requests
import json
import datetime
import time


async def get_currency_rates_from_api(currency_pairs: list) -> dict:
    """
    Асинхронная функция, получающая список с наименованиями валютных пар
    для получения курсов валют по API.

    Args:
        currency_pairs: Список строк, где каждая строка - это пара валют, разделенных '_'.
                        Например: ['USD_EUR', 'USD_KZT'].

    Returns:
        Словарь, где ключ - это пара валют (str), а значение - курс валюты (float)."""
    
    current_date = datetime.date.today()
    rates = {}
    for pair in currency_pairs:
        split_pair = pair.split('_')
        base_currency = split_pair[0]
        conv_currency = split_pair[1]
        try:
            url = f"https://kekkai-api.redume.su/api/getRate/?from_currency={base_currency}&conv_currency={conv_currency}&date={current_date}"
            response = requests.get(url)
            response.raise_for_status()
            todays_rate = response.json().get("rate")
            time.sleep(3)
            pair_dict = {pair: todays_rate}
            rates.update(pair_dict)
            
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
        except json.JSONDecodeError as e:
            print(f"Ошибка при декодировании JSON: {e}")
        except KeyError as e:
            print(f"Ошибка: Ключ 'rate' не найден в JSON ответе: {e}")

    return rates