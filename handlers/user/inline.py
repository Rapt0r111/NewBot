from modules import *
from utils.db_api.get_clothe import get_clothing
from utils.keyboards import NumbersCallbackFactory

router = Router()


@router.callback_query(NumbersCallbackFactory.filter(F.action == "catalog"))  # Получаем тип одежды
async def callbacks_back_floor(callback: types.CallbackQuery, callback_data: NumbersCallbackFactory):
    await callback.message.edit_text(text='Выберите нужный тип одежды', reply_markup=await CATALOG())


@router.callback_query(NumbersCallbackFactory.filter(F.action == "type"))  # Получаем тип одежды
async def callbacks_back_floor(callback: types.CallbackQuery, callback_data: NumbersCallbackFactory):
    await callback.message.edit_text(text='Выберите бренд',
                                     reply_markup=await BRAND(callback_data.value))


@router.callback_query(NumbersCallbackFactory.filter(F.action == "brand"))  # Получаем тип одежды
async def callbacks_back_floor(callback: types.CallbackQuery, callback_data: NumbersCallbackFactory):
    await callback.message.edit_text(text='Выберите принт', reply_markup=await CLOTHE_PRINT(callback_data.value))


@router.callback_query(NumbersCallbackFactory.filter(F.action == "clothes_print"))  # Получаем тип одежды
async def callbacks_back_floor(callback: types.CallbackQuery, callback_data: NumbersCallbackFactory):
    await callback.message.edit_text(text='Выберите цвет', reply_markup=await CLOTHE_COLOR(callback_data.value))


@router.callback_query(NumbersCallbackFactory.filter(F.action == "clothes_color"))  # Получаем тип одежды
async def callbacks_back_floor(callback: types.CallbackQuery, callback_data: NumbersCallbackFactory):
    await callback.message.edit_text(text='Выберите размер', reply_markup=await CLOTHE_SIZE(callback_data.value))


@router.callback_query(NumbersCallbackFactory.filter(F.action == "clothing"))  # Информация об одежде
async def callbacks_back_floor(callback: types.CallbackQuery, callback_data: NumbersCallbackFactory):
    data: dict = (await get_clothing(callback_data.value))[0]
    await callback.message.edit_text(text=f'Тип одежды: {data["type"]}\nБренд: {data["brand"]}\nПринт: '
                                          f'{data["print"]}\nЦвет: {data["color"]}\nРазмер: {data["size"]}\n'
                                          f'Цена: {round(data["price"], 2)}\nСкидка: {round(data["discount"], 2)}',
                                     reply_markup=await BACK_FROM_CATALOG(callback_data.value))

