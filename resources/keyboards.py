import json
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


from config import CURRENSIES_FILE


########################################################################################################
# главное меню
btn_graph_rates = InlineKeyboardButton(text='Получить график', callback_data='graph_rates')
btn_popular_rates = InlineKeyboardButton(text='Популярные курсы', callback_data='popular_rates')

head_menu_inline_btns = [
    btn_graph_rates,
    btn_popular_rates,
]

head_menu_inline_kb = InlineKeyboardBuilder()
head_menu_inline_kb.add(*head_menu_inline_btns)
head_menu_inline_kb.adjust(1)
########################################################################################################
# клавиатура популярных пар
btn_usd_rub = InlineKeyboardButton(text='USD/RUB', callback_data='popular_pair_USD_RUB')
btn_rub_eur = InlineKeyboardButton(text='RUB/EUR', callback_data='popular_pair_RUB_EUR')
btn_eur_usd = InlineKeyboardButton(text='EUR/USD', callback_data='popular_pair_EUR_USD')
btn_usd_kzt = InlineKeyboardButton(text='USD/KZT', callback_data='popular_pair_USD_KZT')
btn_eur_kzt = InlineKeyboardButton(text='EUR/KZT', callback_data='popular_pair_EUR_KZT')

currency_pairs_inline_btns = [
    btn_usd_rub,
    btn_rub_eur,
    btn_eur_usd,
    btn_usd_kzt,
    btn_eur_kzt,
]

currency_pairs_menu_inline_kb = InlineKeyboardBuilder()
currency_pairs_menu_inline_kb.add(*currency_pairs_inline_btns)
currency_pairs_menu_inline_kb.adjust(2)
########################################################################################################
# меню построения графика
btn_week = InlineKeyboardButton(text='Неделя', callback_data='period_week')
btn_month = InlineKeyboardButton(text='Месяц', callback_data='period_month')
btn_year = InlineKeyboardButton(text='Год', callback_data='period_year')

graph_period_menu_inline_btns = [
    btn_week,
    btn_month,
    btn_year,
]

graph_period_menu_inline_kb = InlineKeyboardBuilder()
graph_period_menu_inline_kb.add(*graph_period_menu_inline_btns)
graph_period_menu_inline_kb.adjust(3)
########################################################################################################
# клавиатуры валют

async def creating_base_currency_kb():
    with open(CURRENSIES_FILE, "r", encoding='utf-8') as file:
        names_currencies = json.load(file)

    currencies_btns = []

    for currency_name, currency_code in names_currencies.items():
        btn_currencies = InlineKeyboardButton(text=f'{currency_name}', callback_data=f'base_currency_{currency_code}')
        currencies_btns.append(btn_currencies)

    currencies_kb = InlineKeyboardBuilder()
    currencies_kb.add(*currencies_btns)
    currencies_kb.adjust(2)

    return currencies_kb


async def creating_currency_quotes_kb():
    with open(CURRENSIES_FILE, "r", encoding='utf-8') as file:
        names_currencies = json.load(file)

    currencies_btns = []
    
    for currency_name, currency_code in names_currencies.items():
        btn_currencies = InlineKeyboardButton(text=f'{currency_name}', callback_data=f'currency_quotes_{currency_code}')
        currencies_btns.append(btn_currencies)

    currencies_kb = InlineKeyboardBuilder()
    currencies_kb.add(*currencies_btns)
    currencies_kb.adjust(2)

    return currencies_kb

########################################################################################################