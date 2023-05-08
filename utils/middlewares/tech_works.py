# from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram import types, Dispatcher

from modules import *


async def get_testers() -> List[int]:
    return [451472414,]


class BotMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[types.TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: types.Update,
                       data: Dict[str, Any]
                       ):
        if isinstance(event, types.Message):
            if event.from_user.id in await get_testers():
                return await handler(event, data)
            else:
                await event.answer('<b>⚒ Бот на тех. работах!</b>')

        if isinstance(event, types.CallbackQuery):
            if event.from_user.id in await get_testers():
                return await handler(event, data)
            else:
                await event.answer('⚒ Бот на тех. работах!', True)


def setup(dp: Dispatcher):
    dp.message.middleware(BotMiddleware())
    dp.callback_query.middleware(BotMiddleware())
