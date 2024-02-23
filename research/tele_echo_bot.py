import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
# print(API_TOKEN)

# configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
# bot = Bot(token=TOKEN)
dp = Dispatcher()

# commands=["start", "help"]


@dp.message()
async def command_handler(message: types.Message):
    """
    This handler receives messages with `/start` or  `/help `command
    """
    await message.reply("Hi\nI am Echo Bot!\nCreated By Naren.")


@dp.message()
async def echo(message: types.Message):
    """
    This will retrun echo
    """
    await message.answer(message.text)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
