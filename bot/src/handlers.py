from datetime import datetime
from zoneinfo import ZoneInfo
from aiogram import F, Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from bot.src.database.create_table import execute_query

router = Router()
timestamp_now = datetime.now(tz=ZoneInfo("UTC")).isoformat(" ")


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`

    insert_data(message)
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@router.message(F.text.upper() == "HOW ARE YOU?")
async def how_are_you(message: Message) -> None:

    try:
        insert_data(message)
        await message.answer("I am fine!")
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


@router.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        insert_data(message)
        await message.send_copy(chat_id=message.chat.id)
        await message.answer("Bonnie Scotland! Bon Accord!" +
                             " Alba Since and Forever!" +
                             " Learn this Motto by heart!")
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


def insert_data(message):
    insert_query = (
        f"INSERT INTO messages (message, user_id, message_time) "
        f"VALUES ('{message.text}', {message.from_user.id}, '{timestamp_now}')"
    )
    print(f"VALUES ('{message.text}', {message.from_user.id}, '{timestamp_now}')")
    execute_query(insert_query)
