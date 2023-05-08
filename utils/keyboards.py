from typing import List, Optional

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from modules import types
from utils.db_api.get_clothe import get_clothes_type, get_brand, get_print, get_color, get_size


class NumbersCallbackFactory(CallbackData, prefix="fab"):
    action: str
    value: Optional[int]


async def async_get_inline_keyboard_fab(array: dict,
                                        adjust: int,
                                        action: str,
                                        get_back: str = None,
                                        back_id: int = None,
                                        ) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for key, value in array.items():
        builder.button(text=value,
                       callback_data=NumbersCallbackFactory(
                           action=action,
                           value=key,))
    if get_back:
        builder.button(text="⬅️ Назад",
                       callback_data=NumbersCallbackFactory(
                            action=get_back,
                            value=back_id))
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
    return await async_get_inline_keyboard_fab(options, adjust=1, action="type")


async def brand(clothe_type: int) -> types.InlineKeyboardMarkup:  # Бренды одежды
    options = await get_brand(clothe_type)
    return await async_get_inline_keyboard_fab(options,
                                               adjust=1, action="brand",
                                               get_back="catalog",back_id=clothe_type)


async def clothes_print(clothe_brand: int) -> types.InlineKeyboardMarkup:  # Принты одежды
    options = await get_print(clothe_brand)
    return await async_get_inline_keyboard_fab(options,
                                               adjust=1, action="clothes_print",
                                               get_back="type", back_id=clothe_brand)


async def clothes_color(clothe_print: int) \
        -> types.InlineKeyboardMarkup:  # Цвет одежды
    options = await get_color(clothe_print)
    return await async_get_inline_keyboard_fab(options,
                                               adjust=1, action="clothes_color",
                                               get_back="brand",back_id=clothe_print)


async def clothes_size(clothe_color: int) \
        -> types.InlineKeyboardMarkup:  # Цвет одежды
    options = await get_size(clothe_color)
    return await async_get_inline_keyboard_fab(options,
                                               adjust=1, action="clothing",
                                               get_back="clothes_print", back_id=clothe_color)


async def back_from_catalog(clothe_size: int) \
        -> types.InlineKeyboardMarkup:  # Цвет одежды
    options = {}
    return await async_get_inline_keyboard_fab(options,
                                               adjust=1, action="clothing",
                                               get_back="clothes_color", back_id=clothe_size)


def contact_keyboard() -> types.ReplyKeyboardMarkup:
    first_button = types.KeyboardButton(text="📱 Отправить", request_contact=True)
    back_button = types.KeyboardButton(text="⬅️ Назад")
    builder = ReplyKeyboardBuilder()
    builder.add(first_button)
    builder.add(back_button)
    return builder.as_markup(resize_keyboard=True)
