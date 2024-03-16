import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import  load_dotenv
from os import getenv

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()
#кнопка старта
@dp.message(Command("start"))
async def start(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}")
#кнопка информации
@dp.message(Command("myinfo"))
async def myinfo(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Your ID, {message.from_user.id}")
    await message.answer(f"Your first_name , {message.from_user.first_name}")
    await message.answer(f"Your username , {message.from_user.username}")
#кнопка картинки
@dp.message(Command("pic"))
async def send_pic(message: types.Message):
    file = types.FSInputFile("images/dodo.jpeg")
    await message.answer_photo(file, caption="Dodo")
#рандом картинки hw1
@dp.message(Command("random_pic"))
async def random_pic(message: types.Message):
    file = types.FSInputFile("images/camry.png")
    await message.answer_photo(file, caption="camry")
    file = types.FSInputFile("images/negr.jpeg")
    await message.answer_photo(file, caption="negr")
    file = types.FSInputFile("images/lx 500/jpeg")
    await message.answer_photo(file, caption="lx 500")
    file = types.FSInputFile("images/dodo logo.jpg")
    await message.answer_photo(file, caption="dodo logo")
#эхо текста 
@dp.message()
async def echo(message: types.Message):
    await message.answer("Привет")
    await message.answer(message.text)
    
#запуск бота
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
