from typing import Union

from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton

from BrandrdXMusic.utils import emoji as e


def setting_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["ST_B_1"],
                callback_data="AU",
                icon_custom_emoji_id=e.PROFILE_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_3"],
                callback_data="LG",
                icon_custom_emoji_id=e.GLOBE_ID,
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_2"],
                callback_data="PM",
                icon_custom_emoji_id=e.MUSIC_ID,
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_4"],
                callback_data="VM",
                icon_custom_emoji_id=e.KNOB_ID,
                style=ButtonStyle.SUCCESS,
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


def vote_mode_markup(_, current, mode: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Voting Mode ➜",
                callback_data="VOTEANSWER",
                icon_custom_emoji_id=e.KNOB_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_5"] if mode == True else _["ST_B_6"],
                callback_data="VOMODECHANGE",
                icon_custom_emoji_id=e.CHECK_ID if mode == True else e.BLOCK_ID,
                style=ButtonStyle.SUCCESS if mode == True else ButtonStyle.DANGER,
            ),
        ],
        [
            InlineKeyboardButton(
                text="-2",
                callback_data="FERRARIUDTI M",
                icon_custom_emoji_id=e.THUMBS_DOWN_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=f"Current : {current}",
                callback_data="ANSWERVOMODE",
                icon_custom_emoji_id=e.INFO_ID if hasattr(e, "INFO_ID") else e.EYES_ID,
                style=ButtonStyle.DEFAULT,
            ),
            InlineKeyboardButton(
                text="+2",
                callback_data="FERRARIUDTI A",
                icon_custom_emoji_id=e.CHECK_ID,
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
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


def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["ST_B_7"],
                callback_data="AUTHANSWER",
                icon_custom_emoji_id=e.PROFILE_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_8"] if status == True else _["ST_B_9"],
                callback_data="AUTH",
                icon_custom_emoji_id=e.CROWN_ID if status == True else e.PROFILE_ID,
                style=ButtonStyle.SUCCESS if status == True else ButtonStyle.DANGER,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_1"],
                callback_data="AUTHLIST",
                icon_custom_emoji_id=e.PROFILE_ID,
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
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


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["ST_B_10"],
                callback_data="SEARCHANSWER",
                icon_custom_emoji_id=e.SEARCH_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_11"] if Direct == True else _["ST_B_12"],
                callback_data="MODECHANGE",
                icon_custom_emoji_id=e.BOLT1_ID if Direct == True else e.INBOX_ID,
                style=ButtonStyle.SUCCESS if Direct == True else ButtonStyle.DANGER,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_13"],
                callback_data="AUTHANSWER",
                icon_custom_emoji_id=e.CROWN_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_8"] if Group == True else _["ST_B_9"],
                callback_data="CHANNELMODECHANGE",
                icon_custom_emoji_id=e.CROWN_ID if Group == True else e.PROFILE_ID,
                style=ButtonStyle.SUCCESS if Group == True else ButtonStyle.DANGER,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_14"],
                callback_data="PLAYTYPEANSWER",
                icon_custom_emoji_id=e.MUSIC_ID,
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_8"] if Playtype == True else _["ST_B_9"],
                callback_data="PLAYTYPECHANGE",
                icon_custom_emoji_id=e.CROWN_ID if Playtype == True else e.PROFILE_ID,
                style=ButtonStyle.SUCCESS if Playtype == True else ButtonStyle.DANGER,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
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


def audio_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_8"].format("✅") if low == True else _["ST_B_8"].format("")
                ),
                callback_data="LQA",
                icon_custom_emoji_id=e.CHECK_ID if low == True else e.MUSIC_ID,
                style=ButtonStyle.SUCCESS if low == True else ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_9"].format("✅")
                    if medium == True
                    else _["ST_B_9"].format("")
                ),
                callback_data="MQA",
                icon_custom_emoji_id=e.CHECK_ID if medium == True else e.MUSIC_ID,
                style=ButtonStyle.SUCCESS if medium == True else ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_10"].format("✅")
                    if high == True
                    else _["ST_B_10"].format("")
                ),
                callback_data="HQA",
                icon_custom_emoji_id=e.CHECK_ID if high == True else e.MUSIC_ID,
                style=ButtonStyle.SUCCESS if high == True else ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
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


def video_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_11"].format("✅")
                    if low == True
                    else _["ST_B_11"].format("")
                ),
                callback_data="LQV",
                icon_custom_emoji_id=e.CHECK_ID if low == True else e.MUSIC_ID,
                style=ButtonStyle.SUCCESS if low == True else ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_12"].format("✅")
                    if medium == True
                    else _["ST_B_12"].format("")
                ),
                callback_data="MQV",
                icon_custom_emoji_id=e.CHECK_ID if medium == True else e.MUSIC_ID,
                style=ButtonStyle.SUCCESS if medium == True else ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_13"].format("✅")
                    if high == True
                    else _["ST_B_13"].format("")
                ),
                callback_data="HQV",
                icon_custom_emoji_id=e.CHECK_ID if high == True else e.MUSIC_ID,
                style=ButtonStyle.SUCCESS if high == True else ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
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
