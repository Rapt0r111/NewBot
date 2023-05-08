from modules import *
from handlers import user, admin
from settings.set_commands import set_commands


async def setup():
    dp = Dispatcher()
    dp.include_router(user.router)
    dp.include_router(admin.router)
    bot = Bot(token=config.BOT_TOKEN, parse_mode='html')
    # setting up middlewares 
    # tech_works.setup(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await set_commands(bot)
    await dp.start_polling(bot)

