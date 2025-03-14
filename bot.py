from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import openai
import requests
import sqlite3
from config import TOKEN, OPENAI_API_KEY, INSTAGRAM_API_URL, TIKTOK_API_URL

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

openai.api_key = OPENAI_API_KEY

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("👋 Assalomu alaykum! Xush kelibsiz!

"
                        "🤖 AI Chatbot – Savollar bering
"
                        "📈 Instagram & TikTok xizmatlari
"
                        "💰 Forex & Kripto signallar

"
                        "Kerakli bo‘limni tanlang:")

@dp.message_handler()
async def ai_chat(message: types.Message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message.text}]
    )
    answer = response["choices"][0]["message"]["content"]
    await message.reply(answer)

@dp.message_handler(commands=['instagram', 'tiktok'])
async def social_services(message: types.Message):
    await message.reply("📲 Instagram & TikTok xizmatlari

"
                        "1. Followers – 10,000 so‘m / 100 ta
"
                        "2. Likes – 5,000 so‘m / 100 ta
"
                        "3. Views – 2,000 so‘m / 100 ta

"
                        "Buyurtma berish uchun admin bilan bog‘laning!")

@dp.message_handler(commands=['signals'])
async def trading_signals(message: types.Message):
    await message.reply("📊 Forex & Kripto VIP signallar

"
                        "💎 VIP obuna – 100,000 so‘m / oy
"
                        "💹 Signal namunalari:
"
                        "📈 BTC/USDT – 65,000$ (Buy) 🎯 67,000$ (Target)
"
                        "📉 EUR/USD – 1.0950 (Sell) 🎯 1.0850 (Target)

"
                        "VIP obuna olish uchun /vip_buy tugmasini bosing!")

@dp.message_handler(commands=['vip_buy'])
async def buy_vip(message: types.Message):
    await message.reply("💳 To‘lov tizimini tanlang:

"
                        "1️⃣ Click
"
                        "2️⃣ Payme

"
                        "To‘lovni amalga oshirgach, adminga yozing!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)