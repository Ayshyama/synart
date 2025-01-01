import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiohttp import ClientSession
from dotenv import load_dotenv
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
BACKEND_URL = os.getenv("BACKEND_URL")

if not API_TOKEN:
    print("Error: API_TOKEN is not loaded. Check your .env file.")
    exit(1)

if not BACKEND_URL:
    print("Error: BACKEND_URL is not loaded. Check your .env file.")
    exit(1)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton(
        text="Open Mini App",
        web_app=WebAppInfo(url="http://localhost:5173")  # Update to your frontend's URL
    )
    keyboard.add(web_app_button)

    if BACKEND_URL:
        async with ClientSession() as session:
            payload = {"username": message.from_user.username}
            async with session.post(f"{BACKEND_URL}/user", json=payload) as resp:
                if resp.status == 201:
                    await message.answer("Welcome to SYNART! Your profile has been created.", reply_markup=keyboard)
                elif resp.status == 200:
                    await message.answer("Welcome back to SYNART!", reply_markup=keyboard)
                else:
                    await message.answer("Failed to create your profile. Please try again.", reply_markup=keyboard)
    else:
        await message.answer("Welcome to SYNART! (No backend URL provided)", reply_markup=keyboard)


async def main():
    # Run polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
