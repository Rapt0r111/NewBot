import logging
import os

import asyncpg


async def get_clothes_type() -> dict:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        clothes_types = await conn.fetch(f''' SELECT distinct on (type) type, id  FROM clothes ''')
        return {clothes_types[i]['id']: clothes_types[i]['type'] for i in range(len(clothes_types))}
    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return {'name': 'Ошибка'}


async def get_brand(clothe_type: int) -> dict:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        info = await conn.fetch(f''' SELECT type FROM clothes WHERE id = '{clothe_type}' ''')
        brand = await conn.fetch(f''' SELECT distinct on (brand) id, brand 
                                FROM clothes WHERE type = '{info[0]['type']}' ''')
        return {brand[i]['id']: brand[i]['brand'] for i in range(len(brand))}
    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return {'name': 'Ошибка'}


async def get_print(brand: int) -> dict:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        info = await conn.fetch(f''' SELECT type,brand FROM clothes WHERE id = '{brand}' ''')
        print(f'get_print = {info}')
        clothes_print = await conn.fetch(f''' SELECT distinct on (print) id, print 
                                FROM clothes WHERE type = '{info[0]['type']}' AND brand = '{info[0]['brand']}' ''')
        print(clothes_print)
        return {clothes_print[i]['id']: clothes_print[i]['print'] for i in range(len(clothes_print))}
    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return {'name': 'Ошибка'}


async def get_color(color_id: int) -> dict:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        info = await conn.fetch(f''' SELECT type,brand,print FROM clothes WHERE id = '{color_id}' ''')
        clothes_color = await conn.fetch(f''' SELECT distinct on (color) id, color 
                                FROM clothes WHERE type = '{info[0]['type']}' AND brand = '{info[0]['brand']}' 
                                AND print = '{info[0]['print']}' ''')
        return {clothes_color[i]['id']: clothes_color[i]['color'] for i in range(len(clothes_color))}
    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return {'name': 'Ошибка'}


async def get_size(clothe_size: int) -> dict:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        info = await conn.fetch(f''' SELECT type,brand,print,color FROM clothes WHERE id = '{clothe_size}' ''')
        clothes_size = await conn.fetch(f''' SELECT distinct on (size) id, size 
                                FROM clothes WHERE type = '{info[0]['type']}' AND brand = '{info[0]['brand']}' 
                                AND print = '{info[0]['print']}' AND color = '{info[0]['color']}' ''')
        print(clothes_size)
        return {clothes_size[i]['id']: clothes_size[i]['size'] for i in range(len(clothes_size))}
    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return {'name': 'Ошибка'}


async def get_clothing(clothing_id: int) -> list:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        clothes_size = await conn.fetch(f''' SELECT * FROM clothes WHERE id = '{clothing_id}' ''')
        return clothes_size
    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return ['Ошибка']
