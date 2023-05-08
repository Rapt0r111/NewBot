from typing import List, Optional

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from modules import types
from utils.db_api.get_clothe import get_clothes_type, get_brand, get_print, get_color, get_size


class NumbersCallbackFactory(CallbackData, prefix="fab"):
    action: str
    value: Optional[int]
    type: Optional[int]
    brand: Optional[int]
    c_print: Optional[str]
    c_color: Optional[str]


async def async_get_inline_keyboard_fab(array: dict,
                                        adjust: int,
                                        action: str,
                                        info: dict,
                                        get_back: str = None,
                                        ) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    print(array)
    for key, value in array.items():
        builder.button(text=value,
                       callback_data=NumbersCallbackFactory(
                           action=action,
                           value=key,
                           type=info['c_type'] if 'c_type' in info else None,
                           brand=info['brand'] if 'brand' in info else None,
                           c_print=info['c_print'] if 'c_print' in info else None,
                           c_color=info['c_color'] if 'c_color' in info else None))
    if get_back:
        builder.button(text="⬅️ Назад",
                       callback_data=NumbersCallbackFactory(
                            action=get_back,
                            value=None,
                            type=info['c_type'] if 'c_type' in info else None,
                            brand=info['brand'] if 'brand' in info else None,
                            c_print=info['c_print'] if 'c_print' in info else None,
                            c_color=info['c_color'] if 'c_color' in info else None))
    # Выравниваем кнопки по 2 в ряд
    builder.adjust(adjust)
    return builder.as_markup()


def k_formatter(array: List[list]) -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for row in array:
        for text in row:
            builder.add(types.KeyboardButton(text=str(text)))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def menu() -> types.ReplyKeyboardMarkup:
    options = [
        ["ТРЦ(чат)"], ["Каталог одежды"],
        ["Стать партнёром?"], ["Поиграй-Ка"],
    ]
    return k_formatter(options)


def admin() -> types.ReplyKeyboardMarkup:
    options = [["⬅️ back"]]
    return k_formatter(options)


def back() -> types.ReplyKeyboardMarkup:
    options = [["⬅️ Назад"]]
    return k_formatter(options)


async def catalog() -> types.InlineKeyboardMarkup:  # Каталог типов одежды
    options = await get_clothes_type()  # Получаем все типы одежды
    return await async_get_inline_keyboard_fab(options, adjust=1, action="type", info={})


async def brand(clothe_type: int) -> types.InlineKeyboardMarkup:  # Бренды одежды
    options = await get_brand(clothe_type)
    return await async_get_inline_keyboard_fab(options,
                                               adjust=1, action="brand",
                                               get_back="catalog",
                                               info={"type": clothe_type})


async def clothes_print(clothe_brand: int, brandik: int) -> types.InlineKeyboardMarkup:  # Принты одежды
    options = await get_print(clothe_brand)
    print(f'clothe_brand: {clothe_brand}')
    return await async_get_inline_keyboard_fab(options,
                                               adjust=1, action="clothes_print",
                                               get_back="type",
                                               info={"brand": brandik})


async def clothes_color(clothe_print: int) \
        -> types.InlineKeyboardMarkup:  # Цвет одежды
    options = await get_color(clothe_print)
    return await async_get_inline_keyboard_fab(options,
                                               adjust=1, action="clothes_color",
                                               get_back="brand",
                                               info={"c_print": clothe_print,})


async def clothes_size(clothe_color: int) \
        -> types.InlineKeyboardMarkup:  # Цвет одежды
    options = await get_size(clothe_color)
    return await async_get_inline_keyboard_fab(options,
                                               adjust=1, action="clothes_color",
                                               get_back="clothes_print",
                                               info={"c_color": clothe_color})


def contact_keyboard() -> types.ReplyKeyboardMarkup:
    first_button = types.KeyboardButton(text="📱 Отправить", request_contact=True)
    back_button = types.KeyboardButton(text="⬅️ Назад")
    builder = ReplyKeyboardBuilder()
    builder.add(first_button)
    builder.add(back_button)
    return builder.as_markup(resize_keyboard=True)
