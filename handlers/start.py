from aiogram import Router, F, types
from aiogram.filters import Command
import logging


from keyboards.all_keyboards import start_kb


start_router =  Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
   
    
 #приветствие 
    logging.info(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}", reply_markup=start_kb())
    
    
 


