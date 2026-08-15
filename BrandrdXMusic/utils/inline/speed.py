from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from BrandrdXMusic.utils import emoji as e


def stats_buttons(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["SA_B_1"],
            callback_data="TopOverall",
            icon_custom_emoji_id=e.SPARKLE_ID,
            style=ButtonStyle.PRIMARY,
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_2"],
            callback_data="bot_stats_sudo",
            icon_custom_emoji_id=e.BOLT1_ID,
            style=ButtonStyle.SUCCESS,
        ),
        InlineKeyboardButton(
            text=_["SA_B_3"],
            callback_data="TopOverall",
            icon_custom_emoji_id=e.SPARKLE_ID,
            style=ButtonStyle.PRIMARY,
        ),
    ]
    upl = InlineKeyboardMarkup(
        [
            sudo if status else not_sudo,
            [
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


def back_stats_buttons(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="stats_back",
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
