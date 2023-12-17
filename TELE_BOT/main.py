import asyncio as asy
from aiogram import Bot, Dispatcher, executor

TOKEN = "6839530194:AAGlNCzSH-x09BeMXrSnN8nb9OksJIy7ID8"
loop = asy.get_event_loop()
bot = Bot(TOKEN)
dp = Dispatcher(bot, loop=loop)






if __name__ == "__main__":
    from handler import dp
    executor.start_polling(dp)