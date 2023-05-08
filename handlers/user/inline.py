from modules import *
from utils.keyboards import NumbersCallbackFactory

router = Router()


@router.callback_query(NumbersCallbackFactory.filter(F.action == "catalog"))  # Получаем тип одежды
async def callbacks_back_floor(callback: types.CallbackQuery, callback_data: NumbersCallbackFactory):
    await callback.message.edit_text(text='Выберите нужный тип одежды', reply_markup=await CATALOG())


@router.callback_query(NumbersCallbackFactory.filter(F.action == "type"))  # Получаем тип одежды
async def callbacks_back_floor(callback: types.CallbackQuery, callback_data: NumbersCallbackFactory):
    print(f'type = {callback_data}')
    await callback.message.edit_text(text='Выберите бренд',
                                     reply_markup=await BRAND(
                                         callback_data.value if callback_data.value else callback_data.brand))


@router.callback_query(NumbersCallbackFactory.filter(F.action == "brand"))  # Получаем тип одежды
async def callbacks_back_floor(callback: types.CallbackQuery, callback_data: NumbersCallbackFactory):
    print(f'brand = {callback_data}')
    await callback.message.edit_text(text='Выберите принт', reply_markup=await CLOTHE_PRINT(
        callback_data.value if callback_data.value else callback_data.c_print, callback_data.brand))


@router.callback_query(NumbersCallbackFactory.filter(F.action == "clothes_print"))  # Получаем тип одежды
async def callbacks_back_floor(callback: types.CallbackQuery, callback_data: NumbersCallbackFactory):
    print(f'color = {callback_data}')
    await callback.message.edit_text(text='Выберите цвет', reply_markup=await CLOTHE_COLOR(
        callback_data.value if callback_data.value else callback_data.c_color))


@router.callback_query(NumbersCallbackFactory.filter(F.action == "clothes_color"))  # Получаем тип одежды
async def callbacks_back_floor(callback: types.CallbackQuery, callback_data: NumbersCallbackFactory):
    print(f'size = {callback_data}')
    await callback.message.edit_text(text='Выберите размер', reply_markup=await CLOTHE_SIZE(
        callback_data.value))
