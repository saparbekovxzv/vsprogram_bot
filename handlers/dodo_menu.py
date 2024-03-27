from aiogram import Router,F, types

menu_router = Router()

@menu_router.callback_query(F.data ==  "our_menu")
async def make_order(callback: types.CallbackQuery):
    await callback.message.answer("Какой продукт хотите выбрать?")