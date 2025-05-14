from aiogram import types
from aiogram import Router, F


from resources import (
    currency_pairs_menu_inline_kb,
    choise_popular_pair_text,
    head_menu_inline_kb,
)

from functions import get_currency_rate


router = Router()
    

@router.callback_query(F.data == "popular_rates")
async def f_popular_rates(callback: types.CallbackQuery): 
    await callback.message.delete()
    await callback.message.answer(
        text=choise_popular_pair_text,
        reply_markup=currency_pairs_menu_inline_kb.as_markup(resize_keyboard=True)
        )
    

@router.callback_query(F.data.startswith('popular_pair_'))
async def f_popular_pair(callback: types.CallbackQuery):
    await callback.message.delete()
    popular_pair = callback.data[13:]
    
    rate = await get_currency_rate(popular_pair)
    
    await callback.message.answer(
        text=f'Курс пары {popular_pair} составляет - {rate}',
        reply_markup=head_menu_inline_kb.as_markup(resize_keyboard=True)
        )