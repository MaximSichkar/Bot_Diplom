from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('hello')
