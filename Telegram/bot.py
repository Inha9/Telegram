import logging

from aiogram import Bot, Dispatcher, executor, types
from search_wiki import get_wiki_page

API_TOKEN = '6082663790:AAEqFqwLSIl3kqEZ12d0SFMCqEuIZBoDBs4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
   types.KeyboardButton("WIth Admin")
)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Hi!", reply_markup=menu)

@dp.message_handler(content_types=['WIth Admin'])
async def send_welcome(message: types.Message):
    await message.reply("Bizning admin : link")

@dp.message_handler()
async def echo(message: types.Message):

    text = message.text
    if text == "WIth Admin":
        await message.answer("https://t.me/jamshidkarimov1")
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)