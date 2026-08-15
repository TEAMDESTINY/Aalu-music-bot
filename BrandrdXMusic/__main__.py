import asyncio
import importlib
from sys import argv

from pyrogram import filters, idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from BrandrdXMusic import LOGGER, app, userbot
from BrandrdXMusic.core.call import Hotty
from BrandrdXMusic.misc import sudo
from BrandrdXMusic.plugins import ALL_MODULES
from BrandrdXMusic.utils import emoji as e
from BrandrdXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


@app.on_message(filters.new_chat_members)
async def auto_join_assistant(client, message):
    """Auto-join assistant when bot is added to a group."""
    try:
        if not message.new_chat_members:
            return
        bot_added = any(member.id == app.id for member in message.new_chat_members)
        if not bot_added:
            return
        chat_id = message.chat.id
        try:
            await userbot.join_chat(chat_id)
            LOGGER(__name__).info(f"Assistant joined chat {chat_id}")
        except Exception as exc:
            LOGGER(__name__).warning(f"Assistant join failed for {chat_id}: {exc}")
    except Exception as exc:
        LOGGER(__name__).error(f"auto_join_assistant error: {exc}")


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("BrandrdXMusic.plugins" + all_module)
    LOGGER("BrandrdXMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("BrandrdXMusic").error(
            "Please turn on the videochat of your log group\\channel.\\n\\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    LOGGER("BrandrdXMusic").info(
        f"{e.MUSIC} Bot Started Successfully | {e.BOLT} @BRANDRD_BOT"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("BrandrdXMusic").info("Stopping Brandrd Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
