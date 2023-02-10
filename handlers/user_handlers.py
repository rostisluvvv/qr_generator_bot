from aiogram import Dispatcher
from aiogram.types import Message, ContentType


from lexicon.lexicon import LEXICON
from services.file_handling import generate_qr_code


async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])


async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


async def process_url_command(message: Message):
    await message.answer_photo(generate_qr_code(message.url))


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(process_url_command, content_types=['url'])
