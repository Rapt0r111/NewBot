import asyncio
import logging

import bot
from services import APScheduler


async def main():
    APScheduler.setup()
    await bot.setup()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Приложение остановлено')
