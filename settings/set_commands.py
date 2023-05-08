from aiogram import types, Bot
from aiogram.types import BotCommandScopeDefault

commands = [
    types.BotCommand(command="/start", description="Начать диалог"),
    types.BotCommand(command="/help", description="Помощь"),
]


async def set_commands(bot: Bot):
    await bot.set_my_commands(commands=commands, scope=types.BotCommandScopeDefault())
