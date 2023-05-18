import logging
from aiogram import Bot, Dispatcher, executor, types
from api import get_coffee
logging.basicConfig(level=logging.INFO)
API_TOKEN = 'token yozasan'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("salom men senga coffee yuboraman /cofe bos")
@dp.message_handler(commands="cofe")
async def coffee(message: types.Message):
    rasm=get_coffee()
    await message.answer(rasm)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)