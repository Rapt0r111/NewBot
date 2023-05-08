from filters.isadmin import AdminFilter
from modules import *
from aiogram.filters import StateFilter

router = Router()


@router.message(filters.Command("admin"), F.from_user.id.in_(config.admins), StateFilter(None))
async def cmd_admin(message: types.Message):
    await message.answer('<b>Админ-Панель</b>', reply_markup=ADMIN)


@router.message(filters.Text('⬅️ back'), AdminFilter())
async def cmd_back(message: types.Message, state: FSMContext):
    await message.answer('<b>Меню</b>', reply_markup=MENU)
    await state.clear()
