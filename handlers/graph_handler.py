from aiogram import types
from aiogram import Router, F
from aiogram.types import URLInputFile
from aiogram.fsm.context import FSMContext

from resources import (
    creating_base_currency_kb,
    creating_currency_quotes_kb,
    base_currency_text,
    currency_quotes_text,
    head_menu_inline_kb,
    graph_period_menu_inline_kb,
    choise_period_text,
    rate_not_found_text,
)

from functions import (
    create_graph,
)


router = Router()
    
    
@router.callback_query(F.data == "graph_rates")
async def f_graph_rates(callback: types.CallbackQuery): 
    await callback.message.delete()
    
    base_currencies_kb = await creating_base_currency_kb()

    await callback.message.answer(
        text=base_currency_text,
        reply_markup=base_currencies_kb.as_markup(resize_keyboard=True)
        )


@router.callback_query(F.data.startswith('base_currency_'))
async def f_input_base_currency(callback: types.CallbackQuery, state: FSMContext): 
    await callback.message.delete()
    await state.update_data(base_currency=callback.data[14:])

    currency_quotes_kb = await creating_currency_quotes_kb()

    await callback.message.answer(
        text=currency_quotes_text,
        reply_markup=currency_quotes_kb.as_markup(resize_keyboard=True)
        )


@router.callback_query(F.data.startswith('currency_quotes_'))
async def f_input_currency_quotes(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.update_data(currency_quotes=callback.data[16:]) 
    await callback.message.answer(
        text=choise_period_text,
        reply_markup=graph_period_menu_inline_kb.as_markup(resize_keyboard=True)
        )


@router.callback_query(F.data.startswith('period_'))
async def f_input_period(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.update_data(period=callback.data[7:]) 

    graph_data = await state.get_data()
    graph_link = await create_graph(graph_data['base_currency'], graph_data['currency_quotes'], graph_data['period'])
    
    if graph_link is None:
        await callback.message.answer(
            rate_not_found_text,
            reply_markup=head_menu_inline_kb.as_markup(resize_keyboard=True)
        )

    else:
        img = URLInputFile(graph_link)
        await callback.message.answer_photo(
            photo=img,
            reply_markup=head_menu_inline_kb.as_markup(resize_keyboard=True)
        )