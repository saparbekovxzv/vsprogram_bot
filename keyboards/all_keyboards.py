

from aiogram.types import InlineKeyboardButton ,InlineKeyboardMarkup



def start_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Наш сайт", url="https://dodopizza.kg/bishkek")
            ],
            [
                InlineKeyboardButton(text="Мы в Instagram", url="https://www.instagram.com/dodopizzakg/?hl=ru"),
                InlineKeyboardButton(text="Мы в  Facebook", url="https://www.facebook.com/dodopizzakg/?locale=ru_RU")
            ],
            [
                InlineKeyboardButton(text="О нас",callback_data="about")
            ],
            [
                InlineKeyboardButton(text="Наше меню",callback_data=" our menu")
            ]
            
        ]
    )
    return kb

