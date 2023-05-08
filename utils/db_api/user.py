import logging
import os
import asyncpg
from aiogram import types
from asyncpg import UniqueViolationError


async def create_user(message: types.Message) -> bool:
    username = message.from_user.username if message.from_user.username else None
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        try:
            await conn.execute('''
                    INSERT INTO users (id, name, username) 
                    VALUES($1, $2, $3)''', message.from_user.id, message.from_user.first_name, username)
            return True
        except UniqueViolationError:
            return True

    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return False


async def set_phone_number(user_id: int, phone_number: str) -> bool:
    try:
        conn = await asyncpg.connect(user=os.getenv('user'), database=os.getenv('database'),
                                     password=os.getenv('password'), host=os.getenv('host'))
        if not dict(await conn.fetchrow(f'''SELECT phone_number FROM users  WHERE id = {user_id}'''))["phone_number"]:
            await conn.execute(f'''
                    UPDATE users SET phone_number={phone_number}  WHERE id = {user_id}''')
            return True
        else: return False

    except Exception as e:
        logging.info(f'Не удалось подключиться к базе данных с ошибкой {e}')
        return False
