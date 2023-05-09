import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import (
    BotCommand,
    BotCommandScopeDefault,
    CallbackQuery,
    ChatMemberUpdated,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from magic_filter import F

from dotenv import load_dotenv

import keyboards.main_menu_keyboards as main_menu_keyboards
import keyboards.default_menu_commands as default_menu_commands


router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command.
    """
    await message.answer(
        f"Hello, <b>{message.from_user.full_name}!</b>",
        reply_markup=main_menu_keyboards.main_menu_keyboard
    )
    
@router.message(Command(commands=["about"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/about` command.
    """
    await message.answer(
        f"I'll tell you about all as soon as possible.",
        reply_markup=main_menu_keyboards.main_menu_keyboard,
    )

@router.callback_query(main_menu_keyboards.TapCallback.filter(F.foo=='tap'))
async def callback_tap_me(callback_query: CallbackQuery) -> None:
    await callback_query.answer(
        text="It's 'tap' button",
        show_alert=True
    )
    
@router.callback_query(main_menu_keyboards.TapCallback.filter(F.foo=='click'))
async def callback_tap_me(callback_query: CallbackQuery) -> None:
    await callback_query.answer(
        text="It's 'click' button",
    )


@router.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward received message back to the sender
    By default, message handler will handle all message types (like text, photo, sticker and etc.).
    """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")

async def main() -> None:
    
    bot = Bot(TOKEN, parse_mode="HTML")
    
    await default_menu_commands.set_all_default_commands(bot)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    logging.basicConfig(
        level=logging.INFO,
        filename='ark_bot_log.log',
        filemode='w'
    )
    asyncio.run(main())
