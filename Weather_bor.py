from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from Script_for_weather_API import get_weather
import os


bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)
api_weather_token = os.getenv('api_weather_token')

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.answer('Приветсвую! Напишите название города латиницей, в котором вы хотите узнать погоду!')

@dp.message_handler()
async def start_get_weather(message: types.Message):
    await get_weather(message, api_weather_token)


if __name__ == "__main__":
    executor.start_polling(dp)






