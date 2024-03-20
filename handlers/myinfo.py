from aiogram import Router, types
from aiogram.filters import Command
from os import listdir, path
import logging

myinfo_router = Router()

@myinfo_router.message(Command("myinfo"))
async def myinfo(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Your ID, {message.from_user.id}")
    await message.answer(f"Your first_name , {message.from_user.first_name}")
    await message.answer(f"Your username , {message.from_user.username}")