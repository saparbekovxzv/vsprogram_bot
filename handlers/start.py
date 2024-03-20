from aiogram import Router, types
from aiogram.filters import Command
import logging


start_router =  Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    #кнопки
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="О нас", url="https://dodopizza.kg/bishkek/about")
            ],
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://dodopizza.kg/bishkek")
            ],
            [
                types.InlineKeyboardButton(text="Мы в Instagram", url="https://www.instagram.com/dodopizzakg/?hl=ru"),
                types.InlineKeyboardButton(text="МЫ в  Facebook", url="https://www.facebook.com/dodopizzakg/?locale=ru_RU")
            ]
        ]
    )
   
    #приветствие 
    logging.info(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}", reply_markup=kb)
    
