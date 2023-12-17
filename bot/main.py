import asyncio as asy
from aiogram import Bot, Dispatcher, executor
import os
import speech_recognition as sr

TOKEN = "6839530194:AAGlNCzSH-x09BeMXrSnN8nb9OksJIy7ID8"
loop = asy.get_event_loop()
bot = Bot(TOKEN)
dp = Dispatcher(bot, loop=loop)

from aiogram import types

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):

    await bot.send_message(msg.from_user.id, text="123")

@dp.message_handler(commands=["exitroot"])
async def start(msg: types.Message):
    exit()
    await bot.send_message(msg.from_user.id, text="123")


@dp.message_handler(content_types=['voice'])
async  def d(m: types.Message):
    file_id = m.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, "123.mp3")

    #await bot.download_file((await bot.get_file(m.voice.file_id)).file_path, "123.mp3")
    #asdasd
    i = 0
    a = os.listdir()
    while a[0] != "123.mp3": 
        a = os.listdir()
        i+= 1
        if i == 100:
            break
    else: os.popen("ffmpeg -y -i 123.mp3 123.wav").close()
    i = 0
    a = os.listdir()
    while a[1] != "123.wav":
        a = os.listdir()
        i+= 1
        if i == 100:
            break

    r = sr.Recognizer()
    with sr.AudioFile("123.wav") as s: g = r.record(s)
    text = r.recognize_google(g, language='RU')

    await bot.send_message(m.from_user.id, text)
    os.remove("123.wav")



if __name__ == "__main__":

    executor.start_polling(dp)