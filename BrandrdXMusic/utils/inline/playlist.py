from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from BrandrdXMusic.utils import emoji as e


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_1"],
                callback_data="get_playlist_playmode",
                icon_custom_emoji_id=e.MUSIC_ID,
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                icon_custom_emoji_id=e.BLOCK_ID,
                style=ButtonStyle.DANGER,
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_9"],
                callback_data="SERVERTOP global",
                icon_custom_emoji_id=e.FIRE_ID,
                style=ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_10"],
                callback_data="SERVERTOP chat",
                icon_custom_emoji_id=e.INBOX_ID,
                style=ButtonStyle.SUCCESS,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_11"],
                callback_data="SERVERTOP user",
                icon_custom_emoji_id=e.PROFILE_ID,
                style=ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="get_playmarkup",
                icon_custom_emoji_id=e.CHECK_ID,
                style=ButtonStyle.SUCCESS,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                icon_custom_emoji_id=e.BLOCK_ID,
                style=ButtonStyle.DANGER,
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data="play_playlist a",
                icon_custom_emoji_id=e.MUSIC_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data="play_playlist v",
                icon_custom_emoji_id=e.MUSIC_ID,
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="home_play",
                icon_custom_emoji_id=e.CHECK_ID,
                style=ButtonStyle.SUCCESS,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                icon_custom_emoji_id=e.BLOCK_ID,
                style=ButtonStyle.DANGER,
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="get_top_playlists",
                icon_custom_emoji_id=e.CHECK_ID,
                style=ButtonStyle.SUCCESS,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                icon_custom_emoji_id=e.BLOCK_ID,
                style=ButtonStyle.DANGER,
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["PL_B_7"],
                    callback_data="delete_whole_playlist",
                    icon_custom_emoji_id=e.BOMB1_ID,
                    style=ButtonStyle.DANGER,
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="del_back_playlist",
                    icon_custom_emoji_id=e.CHECK_ID,
                    style=ButtonStyle.SUCCESS,
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    icon_custom_emoji_id=e.BLOCK_ID,
                    style=ButtonStyle.DANGER,
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    icon_custom_emoji_id=e.BLOCK_ID,
                    style=ButtonStyle.DANGER,
                ),
            ]
        ]
    )
    return upl
