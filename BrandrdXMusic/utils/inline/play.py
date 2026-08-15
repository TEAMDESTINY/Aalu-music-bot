import math

from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton

from BrandrdXMusic.utils import emoji as e
from BrandrdXMusic.utils.formatters import time_to_seconds


# Track Markup
def track_markup(_, videoid, user_id, channel, fplay):
    return [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
                icon_custom_emoji_id=e.MUSIC_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                style=ButtonStyle.DANGER,
            )
        ],
    ]


# Stream Timer Markup
def stream_markup_timer(_, vidid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur) or 1
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)

    if 0 < umm <= 10:
        bar = "❥—————————"
    elif 10 < umm < 20:
        bar = "—❥————————"
    elif 20 <= umm < 30:
        bar = "——❥———————"
    elif 30 <= umm < 40:
        bar = "———❥——————"
    elif 40 <= umm < 50:
        bar = "————❥—————"
    elif 50 <= umm < 60:
        bar = "—————❥————"
    elif 60 <= umm < 70:
        bar = "——————❥———"
    elif 70 <= umm < 80:
        bar = "———————❥——"
    elif 80 <= umm < 95:
        bar = "————————❥—"
    else:
        bar = "—————————❥"

    return [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
                style=ButtonStyle.DEFAULT,
            )
        ],
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
                text="Replay",
                callback_data=f"ADMIN Replay|{chat_id}",
                icon_custom_emoji_id=e.REPEAT_ID,
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
            )
        ],
    ]


# Stream Markup
def stream_markup(_, videoid, chat_id):
    return [
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
                text="Replay",
                callback_data=f"ADMIN Replay|{chat_id}",
                icon_custom_emoji_id=e.REPEAT_ID,
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
            )
        ],
    ]


# Playlist Markup
def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    return [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"Playlists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
                icon_custom_emoji_id=e.MUSIC_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"Playlists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                style=ButtonStyle.DANGER,
            ),
        ],
    ]


# Livestream Markup
def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    return [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                style=ButtonStyle.DANGER,
            ),
        ],
    ]


# Slider Markup
def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    return [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
                icon_custom_emoji_id=e.MUSIC_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            InlineKeyboardButton(
                text="Prev",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                style=ButtonStyle.DANGER,
            ),
            InlineKeyboardButton(
                text="Next",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
    ]
