try:
    from pyrogram.enums import ButtonStyle
except ImportError:
    class ButtonStyle:
        PRIMARY = "primary"
        SECONDARY = "secondary"
        SUCCESS = "success"
        DANGER = "danger"
        DEFAULT = "default"

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT
from BrandrdXMusic.utils import emoji as e


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_9"],
                url=SUPPORT_CHAT,
                icon_custom_emoji_id=e.HEART_ID,
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


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Support",
                    url=f"https://t.me/BRANDED_WORLD",
                    icon_custom_emoji_id=e.HEART_ID,
                    style=ButtonStyle.SUCCESS,
                ),
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


def supp_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                    icon_custom_emoji_id=e.HEART_ID,
                    style=ButtonStyle.SUCCESS,
                ),
            ]
        ]
    )
    return upl
