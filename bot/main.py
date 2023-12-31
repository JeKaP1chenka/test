import asyncio as asy
from aiogram import Bot, Dispatcher, executor
import os
import speech_recognition as sr
import sys

# sys.stdout = open('stdout.txt', 'w')
# sys.stderr = open('stderr.txt', 'w')

TOKEN = "6839530194:AAGlNCzSH-x09BeMXrSnN8nb9OksJIy7ID8"
loop = asy.get_event_loop()
bot = Bot(TOKEN)
dp = Dispatcher(bot, loop=loop)

from aiogram import types

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    print("start")
    print("test err", file=sys.stderr)
    await bot.send_message(msg.from_user.id, text="123")

@dp.message_handler(commands=["exitroot"])
async def start(msg: types.Message):
    await bot.send_message(msg.from_user.id, text="123")
    # exit()


@dp.message_handler(content_types=['voice'])
async  def d(m: types.Message):
    file_id = m.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, "123.mp3")
    print(f"{'--'*50}\nfile load", file=sys.stderr)
    #os.system("ls")
    #await bot.download_file((await bot.get_file(m.voice.file_id)).file_path, "123.mp3")
    #asdasd
    i = 0
    a = os.listdir()
    print(a, file=sys.stderr)
    while not "123.mp3" in a: 
        a = os.listdir()
        i+= 1
        if i == 1000:
            return
    os.popen("ffmpeg -y -i 123.mp3 123.wav").close()
    print(f"{'--'*50}\nfile start convert", file=sys.stderr)
    #os.system("ls")
    i = 0
    a = os.listdir()
    while not "123.wav" in a:
        a = os.listdir()
        i+= 1
        if i == 1000:
            return
    print(f"{'--'*50}\nfile end convert", file=sys.stderr)
    #os.system("ls")
    r = sr.Recognizer()
    with sr.AudioFile("123.wav") as s: g = r.record(s)
    text = r.recognize_google(g, language='RU')
    print(f"{'--'*50}\nfile recognizer", file=sys.stderr)
    os.system("ls")
    await bot.send_message(m.from_user.id, text)
    print(f"{'--'*50}\nmsg send", file=sys.stderr)
    #os.system("ls")
    os.remove("123.wav")



if __name__ == "__main__":

    executor.start_polling(dp)