import asyncio
import logging
from aiogram import Bot

# импорты обработчиков
from bot  import bot, dp, db
from handlers.start import start_router
from handlers.dodo_menu import menu_router
from handlers.picture import picture_router
from handlers.random_pic import random_pic_router
from handlers.echo import echo_router
from handlers.myinfo import myinfo_router
from handlers.survey import survey_router

#привязка Базы Данных к боту 
async def on_startup(bot: Bot):
    db.drop_tables()
    db.create_tables()
    db.populate_tables()



async def main():
#регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(picture_router)
    dp.include_router(random_pic_router)
    dp.include_router(myinfo_router)
    dp.include_router(survey_router)
    dp.include_router(echo_router)
    
    dp.startup.register(on_startup)
#запуск бота
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
