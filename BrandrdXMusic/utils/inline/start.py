from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton

import config
from BrandrdXMusic import app
from BrandrdXMusic.utils import emoji as e


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                icon_custom_emoji_id=e.DIAMOND_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                icon_custom_emoji_id=e.HEART_ID,
                style=ButtonStyle.SUCCESS,
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                icon_custom_emoji_id=e.DIAMOND_ID,
                style=ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
                icon_custom_emoji_id=e.BOOK_ID if hasattr(e, "BOOK_ID") else e.SEARCH_ID,
                style=ButtonStyle.SUCCESS,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                user_id=config.OWNER_ID,
                icon_custom_emoji_id=e.CROWN_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                icon_custom_emoji_id=e.HEART_ID,
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_6"],
                url=config.SUPPORT_CHANNEL,
                icon_custom_emoji_id=e.MEGA_ID if hasattr(e, "MEGA_ID") else e.BOLT1_ID,
                style=ButtonStyle.DEFAULT,
            ),
        ],
    ]
    return buttons
