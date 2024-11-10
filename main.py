import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "bot token")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


schedule = {
    "monday_sc": "Математика, Физика",
    "tuesday_sc": "история , биология",
    "wednsday_sc": "История, Литература",
    "thursday_sc": "Отдых",
}

@dp.message(Command("start"))
async def start(message: Message):
    text = f"Hello, {message.from_user.username}! This is your schedule."
    
    markup = InlineKeyboardMarkup(inline_keyboard=[[ 
        InlineKeyboardButton(text="Понедельник", callback_data="monday_sc"),
        InlineKeyboardButton(text="Вторник", callback_data="tuesday_sc"),
        InlineKeyboardButton(text="Среда", callback_data="wednsday_sc"),
        InlineKeyboardButton(text="Четверг", callback_data="thursday_sc")
    ]])
    await message.answer(text=text, reply_markup=markup)


@dp.callback_query(lambda call: call.data in schedule)
async def get_schedule(call: CallbackQuery):
    day_schedule = schedule.get(call.data, "Расписание отсутствует")
    await call.message.answer(text=day_schedule)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
