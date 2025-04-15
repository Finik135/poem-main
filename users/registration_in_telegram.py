from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import requests

TOKEN = "токен_бота"
DJANGO_API_URL = "http://127.0.0.1:8000/poems/home"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.get_args() == "register":
        user_id = message.from_user.id
        username = message.from_user.username

        data = {"telegram_id": user_id, "username": username}
        response = requests.post(DJANGO_API_URL, json=data)

        if response.status_code == 201:
            await message.reply("Ви успішно зареєстровані! Тепер повертайтеся на сайт.")
        else:
            await message.reply("Помилка при реєстрації. Спробуйте ще раз.")

if __name__ == '__main__':
    executor.start_polling(dp)