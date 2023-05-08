import logging
import os

import asyncpg


async def get_user(user_id: int) -> dict:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        shops = await conn.fetchrow(f''' SELECT name,username,coupons,rating,wins,phone_number 
        FROM users WHERE id = '{user_id}' ''')
        return dict(shops)
    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return {"name": "Ошибочка", "description": "Ошибочка"}
