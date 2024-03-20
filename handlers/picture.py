from aiogram import Router, types
from aiogram.filters import Command
from os import listdir, path
import logging
from pathlib import Path



picture_router = Router()


@picture_router.message(Command("pic"))
async def send_pic(message: types.Message):
 #  file_name =  listdir("images")
    file_name = list((Path(__file__).parent.parent/ "images").iterdir())[0]
    file_path = Path(__file__).parent.parent / "images" / "camry.png"
    logging.info(file_path)
 #  file_path = path.join("images", file_name)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file, caption="car")
