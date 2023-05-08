import aiogram, logging
from typing import *

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types, filters

from aiogram.fsm.context import FSMContext
# #from aiogram.contrib.fsm_storage.mongo import MongoStorage

from settings import config
from utils.keyboards import clothes_print, clothes_color, clothes_size, back_from_catalog
from utils.middlewares import tech_works

from utils import keyboards

# logger setting up
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

# bot setting up

# keyboards setting up
MENU = keyboards.menu()
ADMIN = keyboards.admin()
BACK: ReplyKeyboardMarkup = keyboards.back()
CATALOG = keyboards.catalog
BRAND = keyboards.brand
CLOTHE_PRINT = clothes_print
CLOTHE_COLOR = clothes_color
CLOTHE_SIZE = clothes_size
BACK_FROM_CATALOG = back_from_catalog
