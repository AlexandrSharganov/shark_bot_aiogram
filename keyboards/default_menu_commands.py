from aiogram import Bot
from aiogram.types import(
    BotCommand,
    BotCommandScopeDefault,
)

DEFAULT_COMMANDS = [
    BotCommand(command='start', description='Запустить(перезапустить) бота♻️'),
    BotCommand(command='about', description='Описание бота📄'),
    BotCommand(command='help', description='Помощь🆘'),
    
]
        
async def set_all_default_commands(bot: Bot):
    await bot.set_my_commands(
        commands=DEFAULT_COMMANDS,
        scope = BotCommandScopeDefault()
    )