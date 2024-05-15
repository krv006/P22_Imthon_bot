from datetime import datetime

from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import redis
from filtres import IsAdmin

ADMIN = 1305675046,

main_router = Router()


@main_router.message(F.text.startswith('/stat'), IsAdmin(ADMIN))
async def register(message: Message):
    users = redis.get('users')
    user = message.text.split()[-1]
    for i in users.items():
        if i[0] == user:
            await message.answer(f"{i[1]}")
            return
    await message.answer("Bu user register bolmagan!!!")
    redis['users'] = users


@main_router.message(IsAdmin(ADMIN), F.text.startswith('/send'))
async def send(message: Message, bot: Bot):
    try:
        user_id = message.text.split()[1]
        msg = message.text.split(maxsplit=2)[-1]
        await bot.send_message(chat_id=user_id, text=msg)
    except IndexError:
        await message.reply("Xato: Foydalanuvchi identifikatori va xabar to'g'ri kiritilmagan.")


@main_router.message(CommandStart())
async def start(message: Message):
    users = redis.get('users')
    user_id = str(message.from_user.id)
    users[user_id] = datetime.now().strftime("%Y-%m-%d %H:%M:%S"[:-3])
    redis['users'] = users
    await message.answer(f"Assalomu alaykum, <b>{message.from_user.full_name}</b>!\nBizning botimizga xush kelibsiz")
