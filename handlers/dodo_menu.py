from aiogram import Router,F, types

menu_router = Router()

@menu_router.callback_query(F.data ==  "our_menu")
async def make_order(callback: types.CallbackQuery):
    #кнопки
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
             types.KeyboardButton(text="Комбо")
            ],
            [
             types.KeyboardButton(text="Пицца 25 см"),
             types.KeyboardButton(text="Пицца 30 см"),
             types.KeyboardButton(text="Пицца 35 см"),
            ],
            [
             types.KeyboardButton(text="Закуски")
            ],
            [
             types.KeyboardButton(text="Кофе")
            ],
            [
             types.KeyboardButton(text="Коктейли")
            ],
            [
             types.KeyboardButton(text="Напитки")
            ],
            [
             types.KeyboardButton(text="Десерты")
            ],
            [
             types.KeyboardButton(text="Соусы")
            ],
            [
             types.KeyboardButton(text="Другие товары")
            ]
        ]
    )
    await callback.message.answer("Какой продукт хотите выбрать?", reply_markup=kb)
    
#обработчики
@menu_router.message(F.text.lower() == "комбо")
async def show_pizzas(message: types.Message):
    await message.answer("Комбо которые мы можем предложить!")
    
@menu_router.message(F.text.lower() == "пицца 25 см")
async def show_pizzas(message: types.Message):
    await message.answer("Пиццы которые мы можем предложить!")
    
@menu_router.message(F.text.lower() == "пицца 30 см")
async def show_pizzas(message: types.Message):
    await message.answer("Пиццы которые мы можем предложить!")
    
@menu_router.message(F.text.lower() == "пицца 35 см")
async def show_pizzas(message: types.Message):
    await message.answer("Пиццы которые мы можем предложить!")
    
@menu_router.message(F.text.lower() == "закуски")
async def show_pizzas(message: types.Message):
    await message.answer("Закуски которые мы можем предложить!")
    
@menu_router.message(F.text.lower() == "кофе")
async def show_pizzas(message: types.Message):
    await message.answer("Кофе которые мы можем предложить!")
    
@menu_router.message(F.text.lower() == "коктейли")
async def show_pizzas(message: types.Message):
    await message.answer("Коктейли которые мы можем предложить!")

@menu_router.message(F.text.lower() == "напитки")
async def show_pizzas(message: types.Message):
    await message.answer("Напитки которые мы можем предложить!")
    
@menu_router.message(F.text.lower() == "десерты")
async def show_pizzas(message: types.Message):
    await message.answer("Десерты которые мы можем предложить!")
    
@menu_router.message(F.text.lower() == "соусы")
async def show_pizzas(message: types.Message):
    await message.answer("Соусы которые мы можем предложить!")
    
@menu_router.message(F.text.lower() == "другие товары")
async def show_pizzas(message: types.Message):
    await message.answer("Другие товары которые мы можем предложить!")