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
    await message.answer('Добро пожаловать!', reply_markup=MENU)
    # else:
    #     await message.answer('<b>Технические неполадки...</b>')


@router.message(filters.Text("ТРЦ(чат)"), StateFilter(None))
async def cmd_start(message: types.Message):
    await message.answer('Следуйте правилам чата в закреплённом сообщении!\n Чат - https://t.me/torguem_i_razvlekaemsia/38')


@router.message(filters.Text("Стать партнёром?"), StateFilter(None))
async def cmd_start(message: types.Message):
    await message.answer('Для того, чтобы стать партнёром, заполните [анкету](https://docs.google.com/forms/d/e/1FAIpQLSeZ9xBluMn-QvXn4oaGWNUiqac2IS8VBPUQuGKBlfmyJPolrw/viewform?usp=sf_link) для заявки. Мы свяжемся с вами сразу, как просмотрим вашу анкету!', parse_mode='Markdown')


@router.message(filters.Text("Поиграй-Ка"), StateFilter(None))
async def cmd_start(message: types.Message):
    await message.answer('Выберите игру, в которой хотите посоревноваться за приятные подарки!')





