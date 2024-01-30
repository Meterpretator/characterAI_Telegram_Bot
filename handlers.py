from aiogram import F, Router, types, flags
from aiogram.filters import Command
from aiogram.types import Message

from utils import char_response

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(char_response(f'My name is {msg.from_user.username}. Introduce yourself.'))


@router.message()
async def text_generate(msg: Message):
    await msg.answer(char_response(msg.text))