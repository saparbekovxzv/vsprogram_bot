from aiogram import Router, types
from aiogram.filters import Command
from os import listdir, path
import logging
import random
import os

random_pic_router = Router()

@random_pic_router.message(Command("random_pic"))
async def random_pic(message: types.Message):
    image_folder = "images"
    images = [os.path.join(image_folder, file) for file in os.listdir(image_folder)]
    random_pic = random.choice(images)

 
     #file = types.FSInputFile(filename=random.choice("images"))
      # await message.answer_photo(file)
     