try:
    from pyrogram.enums import ButtonStyle
except ImportError:
    class ButtonStyle:
        PRIMARY = "primary"
        SECONDARY = "secondary"
        SUCCESS = "success"
        DANGER = "danger"
        DEFAULT = "default"

from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from BrandrdXMusic import app
from BrandrdXMusic.utils import emoji as e


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"],
            callback_data=f"close",
            icon_custom_emoji_id=e.BLOCK_ID,
            style=ButtonStyle.DANGER,
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_PAGE"],
            callback_data=f"mbot_cb",
            icon_custom_emoji_id=e.NOTE_ID,
            style=ButtonStyle.PRIMARY,
        ),
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
            icon_custom_emoji_id=e.CHECK_ID,
            style=ButtonStyle.SUCCESS,
        ),
        InlineKeyboardButton(
            text=_["NEXT_PAGE"],
            callback_data=f"mbot_cb",
            icon_custom_emoji_id=e.BOLT1_ID,
            style=ButtonStyle.PRIMARY,
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                    icon_custom_emoji_id=e.CROWN_ID,
                    style=ButtonStyle.PRIMARY,
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                    icon_custom_emoji_id=e.PROFILE_ID,
                    style=ButtonStyle.PRIMARY,
                ),
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="help_callback hb3",
                    icon_custom_emoji_id=e.BOLT1_ID,
                    style=ButtonStyle.PRIMARY,
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="help_callback hb4",
                    icon_custom_emoji_id=e.BLOCK_ID,
                    style=ButtonStyle.PRIMARY,
                ),
                InlineKeyboardButton(
                    text=_["H_B_5"],
                    callback_data="help_callback hb5",
                    icon_custom_emoji_id=e.BLOCK_ID,
                    style=ButtonStyle.PRIMARY,
                ),
                InlineKeyboardButton(
                    text=_["H_B_6"],
                    callback_data="help_callback hb6",
                    icon_custom_emoji_id=e.INBOX_ID,
                    style=ButtonStyle.PRIMARY,
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_7"],
                    callback_data="help_callback hb7",
                    icon_custom_emoji_id=e.BOMB1_ID,
                    style=ButtonStyle.SUCCESS,
                ),
                InlineKeyboardButton(
                    text=_["H_B_8"],
                    callback_data="help_callback hb8",
                    icon_custom_emoji_id=e.REPEAT_ID,
                    style=ButtonStyle.SUCCESS,
                ),
                InlineKeyboardButton(
                    text=_["H_B_9"],
                    callback_data="help_callback hb9",
                    icon_custom_emoji_id=e.KNOB_ID,
                    style=ButtonStyle.SUCCESS,
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_10"],
                    callback_data="help_callback hb10",
                    icon_custom_emoji_id=e.BOLT1_ID,
                    style=ButtonStyle.SUCCESS,
                ),
                InlineKeyboardButton(
                    text=_["H_B_11"],
                    callback_data="help_callback hb11",
                    icon_custom_emoji_id=e.MUSIC_ID,
                    style=ButtonStyle.SUCCESS,
                ),
                InlineKeyboardButton(
                    text=_["H_B_12"],
                    callback_data="help_callback hb12",
                    icon_custom_emoji_id=e.SPARKLE_ID,
                    style=ButtonStyle.SUCCESS,
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_13"],
                    callback_data="help_callback hb13",
                    icon_custom_emoji_id=e.SEARCH_ID,
                    style=ButtonStyle.DANGER,
                ),
                InlineKeyboardButton(
                    text=_["H_B_14"],
                    callback_data="help_callback hb14",
                    icon_custom_emoji_id=e.MUSIC_ID,
                    style=ButtonStyle.DANGER,
                ),
                InlineKeyboardButton(
                    text=_["H_B_15"],
                    callback_data="help_callback hb15",
                    icon_custom_emoji_id=e.BOLT2_ID,
                    style=ButtonStyle.DANGER,
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                    icon_custom_emoji_id=e.CHECK_ID,
                    style=ButtonStyle.SUCCESS,
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
                icon_custom_emoji_id=e.SEARCH_ID,
                style=ButtonStyle.PRIMARY,
            ),
        ],
    ]
    return buttons
