from pyrogram import filters
from pyrogram.enums import ButtonStyle, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from BrandrdXMusic import app
from BrandrdXMusic.utils import emoji as e


@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message

    if reply:
        user_id = reply.from_user.id
        user_name = reply.from_user.first_name
        text = (
            f"{e.PROFILE} <b>User ID</b>\n\n"
            f"<b>Name :</b> {user_name}\n"
            f"<b>ID :</b> <code>{user_id}</code>\n\n"
            f"{e.SPARKLE} <i>Tap on the ID to copy</i>"
        )
        button = InlineKeyboardButton(
            "Close",
            callback_data="close",
            icon_custom_emoji_id=e.BLOCK_ID,
            style=ButtonStyle.DANGER,
        )
        markup = InlineKeyboardMarkup([[button]])
        message.reply_text(
            text,
            reply_markup=markup,
            parse_mode=ParseMode.HTML,
        )
    else:
        chat_id = message.chat.id
        text = (
            f"{e.INBOX} <b>Chat ID</b>\n\n"
            f"<b>ID :</b> <code>{chat_id}</code>\n\n"
            f"{e.SPARKLE} <i>Tap on the ID to copy</i>"
        )
        button = InlineKeyboardButton(
            "Close",
            callback_data="close",
            icon_custom_emoji_id=e.BLOCK_ID,
            style=ButtonStyle.DANGER,
        )
        markup = InlineKeyboardMarkup([[button]])
        message.reply(
            text,
            reply_markup=markup,
            parse_mode=ParseMode.HTML,
        )
