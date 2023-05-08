import logging
import os

import asyncpg


async def get_clothes_type() -> dict:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        clothes_types = await conn.fetch(f''' SELECT id, name FROM clothing_types ''')
        return {clothes_types[i]['id']: clothes_types[i]['name'] for i in range(len(clothes_types))}
    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return {'name': 'Ошибка'}


async def get_brand(clothe_type: int) -> dict:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        brand = await conn.fetch(f''' SELECT id, name FROM clothing_brands WHERE clothes_type_id = '{clothe_type}' ''')
        return {brand[i]['id']: brand[i]['name'] for i in range(len(brand))}
    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return {'name': 'Ошибка'}


async def get_print(brand: int) -> dict:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        clothes_print = await conn.fetch(f''' SELECT id, name FROM 
                                        clothing_prints WHERE clothing_brands_id = '{brand}' ''')
        return {clothes_print[i]['id']: clothes_print[i]['name'] for i in range(len(clothes_print))}
    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return {'name': 'Ошибка'}


async def get_color(color_id: int) -> dict:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        clothes_color = await conn.fetch(f''' SELECT id, name FROM 
                                        clothing_colors WHERE clothing_prints_ids = '{color_id}' ''')
        return {clothes_color[i]['id']: clothes_color[i]['name'] for i in range(len(clothes_color))}
    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return {'name': 'Ошибка'}


async def get_size(clothe_size: int) -> dict:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        clothes_size = await conn.fetch(f''' SELECT id, name FROM 
                                        clothing_sizes WHERE clothing_cloros_id = '{clothe_size}' ''')
        return {clothes_size[i]['id']: clothes_size[i]['name'] for i in range(len(clothes_size))}
    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return {'name': 'Ошибка'}
