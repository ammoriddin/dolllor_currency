import requests
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def salom(message: types.Message):
    await message.reply("Salom botimizga xush kelibsiz!!")

@dp.message_handler(commands=['help'])
async def yordam(message: types.Message):
    await message.reply("botimiz sizga 1dollir necha so'm ligini aytib beradi")



@dp.message_handler(commands=['dollar'])
async def kurslar(message: types.Message):
    API_KEY = ''
    curresy = 'USD'
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{curresy}/UZS'
    r = requests.get(url)
    kurs = r.json()['conversion_rate']
    print(f'bugungi kurs: 1AQSH dollar = {kurs} so\'m')

    await message.answer(f'bugungi kurs: 1AQSH dollir= {(kurs)} so\'m')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
