import asyncio

from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')

# getting
BOT_TOKEN = getenv('BOT_TOKEN')

USER = getenv('user')
PSWD = getenv('password')
DB = getenv('database')
HOST = getenv('host')

admins = {
    451472414,
}
