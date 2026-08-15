import random

from pyrogram import Client, filters
from pyrogram.enums import ButtonStyle, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import LOGGER_ID as LOG_GROUP_ID
from BrandrdXMusic import app
from BrandrdXMusic.core.userbot import Userbot
from BrandrdXMusic.utils import emoji as e
from BrandrdXMusic.utils.database import delete_served_chat, get_assistant


photo = [
    "https://te.legra.ph/file/758a5cf4598f061f25963.jpg",
    "https://te.legra.ph/file/30a1dc870bd1a485e3567.jpg",
    "https://te.legra.ph/file/d585beb2a6b3f553299d2.jpg",
    "https://te.legra.ph/file/7df9e128dd261de2afd6b.jpg",
    "https://te.legra.ph/file/f60ebb75ad6f2786efa4e.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "Private Group"
                )
                msg = (
                    f"{e.MUSIC} <b>Music Bot Added In A New Group</b>\n\n"
                    f"{e.PIN} <b>Chat Name:</b> {message.chat.title}\n"
                    f"{e.IDCARD if hasattr(e, 'IDCARD') else e.INBOX} <b>Chat ID:</b> <code>{message.chat.id}</code>\n"
                    f"{e.GLOBE} <b>Chat Username:</b> @{username}\n"
                    f"{e.PEOPLE if hasattr(e, 'PEOPLE') else e.PROFILE} <b>Group Members:</b> {count}\n"
                    f"{e.CROWN} <b>Added By:</b> {message.from_user.mention}"
                )
                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=random.choice(photo),
                    caption=msg,
                    parse_mode=ParseMode.HTML,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Added By",
                                    url=f"tg://openmessage?user_id={message.from_user.id}",
                                    icon_custom_emoji_id=e.CROWN_ID,
                                    style=ButtonStyle.PRIMARY,
                                )
                            ]
                        ]
                    ),
                )
                await userbot.join_chat(f"{username}")
    except Exception as e:
        print(f"Error: {e}")
