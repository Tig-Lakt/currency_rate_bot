from aiogram import types
from aiogram import Router
from aiogram.filters.command import Command


from resources import (
    welcome_text,
    head_menu_inline_kb,
)


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обработчик команды `/start`.

    Приветствует пользователя и предлагает выбрать дальнейшее действие.

    Args:
        message (types.Message): Объект сообщения от пользователя.
    """
    
    await message.answer(text=welcome_text,
                             reply_markup=head_menu_inline_kb.as_markup(resize_keyboard=True))