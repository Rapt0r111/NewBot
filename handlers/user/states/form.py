from modules import * 
from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    name = State()
    age = State()

router = Router()

router.message.filter(filters.StateFilter(Form))


@router.message(Form.name)
async def form(message: types.Message, state: FSMContext):
    await message.answer('Теперь введи возраст:')
    await state.update_data(name=message.text)
    await state.set_state(Form.age)

@router.message(Form.age)
async def form(message: types.Message, state: FSMContext):
    await message.answer(f'Твои данные\n\n{(await state.get_data())["name"]} Возраст: {message.text}')
    await state.clear()