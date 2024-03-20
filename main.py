import asyncio
import logging

# импорты обработчиков
from bot  import bot, dp
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.random_pic import random_pic_router
from handlers.echo import echo_router
from handlers.myinfo import myinfo_router

    
async def main():
#регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(random_pic_router)
    dp.include_router(myinfo_router)
    dp.include_router(echo_router)
    
#запуск бота
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
