from aiogram.filters import StateFilter

from modules import *
from utils import functions
from utils.db_api.user import create_user

router = Router()


@router.message(filters.Text('⬅️ Назад'))
async def cmd_back(message: types.Message, state: FSMContext):
    await message.answer('<b>Меню</b>', reply_markup=MENU)
    await state.clear()


@router.message(filters.Command("start"), StateFilter(None))
async def cmd_start(message: types.Message):
    # if await create_user(message):
    await message.answer('Дороу', reply_markup=MENU)
    # else:
    #     await message.answer('<b>Технические неполадки...</b>')


@router.message(filters.Text("ТРЦ(чат)"), StateFilter(None))
async def cmd_start(message: types.Message):
    await message.answer('Чат - {?}')


@router.message(filters.Text("Стать партнёром?"), StateFilter(None))
async def cmd_start(message: types.Message):
    await message.answer('<b> text</b>')


@router.message(filters.Text("Поиграй-Ка"), StateFilter(None))
async def cmd_start(message: types.Message):
    await message.answer('Бот с играми - {?}')





