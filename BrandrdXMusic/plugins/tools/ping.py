from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from BrandrdXMusic import app
from BrandrdXMusic.core.call import Hotty
from BrandrdXMusic.utils import bot_sys_stats
from BrandrdXMusic.utils import emoji as e
from BrandrdXMusic.utils.decorators.language import language
from BrandrdXMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
        parse_mode=ParseMode.HTML,
    )
    pytgping = await Hotty.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    text = (
        f"{e.BOLT} <b>Pong:</b> <code>{resp}ms</code>\n\n"
        f"{e.MUSIC} <b>{app.mention} System Stats:</b>\n\n"
        f"{e.SPARKLE} <b>Uptime:</b> {UP}\n"
        f"{e.SNOW if hasattr(e, 'SNOW') else e.CLOCK} <b>RAM:</b> {RAM}\n"
        f"{e.FIRE} <b>CPU:</b> {CPU}\n"
        f"{e.INBOX} <b>Disk:</b> {DISK}\n"
        f"{e.HEAD if hasattr(e, 'HEAD') else e.MUSIC} <b>Py-TgCalls:</b> <code>{pytgping}ms</code>"
    )
    await response.edit_text(
        text,
        parse_mode=ParseMode.HTML,
        reply_markup=supp_markup(_),
    )
