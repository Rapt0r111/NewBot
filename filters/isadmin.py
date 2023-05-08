from aiogram.filters import BaseFilter

from modules import *


class AdminFilter(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id in config.admins