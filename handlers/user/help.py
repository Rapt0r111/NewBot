from modules import *

router = Router()


@router.message(filters.Command('help'))
async def cmd_admin(message: types.Message):
    await message.answer('<b>Помощь</b>', reply_markup=BACK)

