from pyrogram.enums import ButtonStyle, ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from youtubesearchpython.__future__ import VideosSearch

from BrandrdXMusic import app
from BrandrdXMusic.utils import emoji as e
from BrandrdXMusic.utils.inlinequery import answer
from config import BANNED_USERS


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await client.answer_inline_query(query.id, results=answer, cache_time=10)
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[0]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} Mins | {channel} | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="YouTube",
                            url=link,
                            icon_custom_emoji_id=e.MUSIC_ID,
                            style=ButtonStyle.PRIMARY,
                        )
                    ],
                ]
            )
            searched_text = (
                f"{e.MUSIC} <b>Title :</b> <a href={link}>{title}</a>\n\n"
                f"{e.CLOCK} <b>Duration :</b> {duration} Mins\n"
                f"{e.EYES} <b>Views :</b> <code>{views}</code>\n"
                f"{e.BOLT} <b>Channel :</b> <a href={channellink}>{channel}</a>\n"
                f"{e.PIN} <b>Published On :</b> {published}\n\n"
                f"{e.SPARKLE} <b>➻ Inline Search Mode By {app.name}</b>"
            )
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await client.answer_inline_query(query.id, results=answers)
        except:
            return
