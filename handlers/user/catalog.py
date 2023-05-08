from aiogram.filters import StateFilter

from modules import *
from utils.db_api.get_clothe import get_clothes_type

router = Router()


@router.message(filters.Text('Каталог одежды'), StateFilter(None))
async def set_floor(message: types.Message):
    await message.answer('Выберите нужный тип одежды:', reply_markup=await CATALOG())
