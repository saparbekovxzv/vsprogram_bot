from aiogram import Router, types
from aiogram.filters import Command
from os import listdir, path
import logging


random_pic_router = Router()

@random_pic_router.message(Command("random_pic"))
async def random_pic(message: types.Message):
    file = types.FSInputFile("images/camry.png")
    await message.answer_photo(file, caption="camry")
    file = types.FSInputFile("images/negr.jpeg")
    await message.answer_photo(file, caption="negr")
    file = types.FSInputFile("images/lx500/jpeg")
    await message.answer_photo(file, caption="lx 500")
    file = types.FSInputFile("images/dodo.logo.jpg")
    await message.answer_photo(file, caption="dodo logo")
    
