from main import bot, dp


from aiogram import types


@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await bot.send_message(msg.from_user.id, text="введите имя")
    await bot.send_message(msg.from_user.id, text="123")

