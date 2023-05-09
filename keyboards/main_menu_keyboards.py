from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.filters.callback_data import CallbackData



class TapCallback(CallbackData, prefix="my"):
    foo: str


main_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Tap me, bro",
                callback_data=TapCallback(foo="tap").pack()
            ),
            InlineKeyboardButton(
                text="Click me, bro",
                callback_data=TapCallback(foo="click").pack()
            )
        ]
    ]
)