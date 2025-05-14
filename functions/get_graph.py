import requests
import json


async def create_graph(base_currency: str, conv_currency: str, period: str) -> str | None:
    """
    Асинхронно получает ссылку на график, отображающий изменение курса одной валюты относительно другой за 
    определенный период времени, используя API `kekkai-api.redume.su`.

    Args:
        base_currency: Код базовой валюты (например, "USD").
        conv_currency: Код валюты конвертации (например, "EUR").
        period: Период времени, за который необходимо получить график (например, "week" - 1 неделя, "month" - 1 месяц).

    Returns:
        Ссылка на график в формате URL (str), если запрос выполнен успешно и API вернул ссылку.
        Возвращает None в случае ошибки при выполнении запроса, декодировании JSON или отсутствии 
        ключа 'detail' в JSON ответе."""
    
    try:
        url = f"https://kekkai-api.redume.su/api/getChart/{period}?from_currency={base_currency}&conv_currency={conv_currency}"
        response = requests.get(url)
        response.raise_for_status()
        graph_link = response.json().get("detail")
        return graph_link
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
    except json.JSONDecodeError as e:
        print(f"Ошибка при декодировании JSON: {e}")
    except KeyError as e:
        print(f"Ошибка: Ключ 'detail' не найден в JSON ответе: {e}")