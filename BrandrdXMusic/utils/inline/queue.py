from typing import Union

from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from BrandrdXMusic import app
from BrandrdXMusic.utils import emoji as e


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
            ),
        ]
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
                style=ButtonStyle.DEFAULT,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                    style=ButtonStyle.SUCCESS,
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=ButtonStyle.DANGER,
                ),
            ]
        ]
    )
    return upl


def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="Resume",
                callback_data=f"ADMIN Resume|{chat_id}",
                icon_custom_emoji_id=e.MUSIC_ID,
                style=ButtonStyle.SUCCESS,
            ),
            InlineKeyboardButton(
                text="Pause",
                callback_data=f"ADMIN Pause|{chat_id}",
                icon_custom_emoji_id=e.NOTE_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text="Skip",
                callback_data=f"ADMIN Skip|{chat_id}",
                icon_custom_emoji_id=e.BOLT1_ID,
                style=ButtonStyle.DANGER,
            ),
            InlineKeyboardButton(
                text="Stop",
                callback_data=f"ADMIN Stop|{chat_id}",
                icon_custom_emoji_id=e.BLOCK_ID,
                style=ButtonStyle.DANGER,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
            ),
        ],
    ]
    return buttons


def queuemarkup(_, vidid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            InlineKeyboardButton(
                text="Pause",
                callback_data=f"ADMIN Pause|{chat_id}",
                icon_custom_emoji_id=e.NOTE_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text="Stop",
                callback_data=f"ADMIN Stop|{chat_id}",
                icon_custom_emoji_id=e.BLOCK_ID,
                style=ButtonStyle.DANGER,
            ),
            InlineKeyboardButton(
                text="Skip",
                callback_data=f"ADMIN Skip|{chat_id}",
                icon_custom_emoji_id=e.BOLT1_ID,
                style=ButtonStyle.DANGER,
            ),
        ],
        [
            InlineKeyboardButton(
                text="Resume",
                callback_data=f"ADMIN Resume|{chat_id}",
                icon_custom_emoji_id=e.MUSIC_ID,
                style=ButtonStyle.SUCCESS,
            ),
            InlineKeyboardButton(
                text="Replay",
                callback_data=f"ADMIN Replay|{chat_id}",
                icon_custom_emoji_id=e.REPEAT_ID,
                style=ButtonStyle.PRIMARY,
            ),
        ],
    ]
    return buttons
