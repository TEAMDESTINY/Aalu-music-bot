from typing import Union

from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton


def setting_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["ST_B_1"],
                callback_data="AU",
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_3"],
                callback_data="LG",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_2"],
                callback_data="PM",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_4"],
                callback_data="VM",
                style=ButtonStyle.SUCCESS,
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


def vote_mode_markup(_, current, mode: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Voting Mode ➜",
                callback_data="VOTEANSWER",
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_5"] if mode == True else _["ST_B_6"],
                callback_data="VOMODECHANGE",
                style=ButtonStyle.SUCCESS if mode == True else ButtonStyle.DANGER,
            ),
        ],
        [
            InlineKeyboardButton(
                text="-2",
                callback_data="FERRARIUDTI M",
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=f"Current : {current}",
                callback_data="ANSWERVOMODE",
                style=ButtonStyle.DEFAULT,
            ),
            InlineKeyboardButton(
                text="+2",
                callback_data="FERRARIUDTI A",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
                style=ButtonStyle.SUCCESS,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
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
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_8"] if status == True else _["ST_B_9"],
                callback_data="AUTH",
                style=ButtonStyle.SUCCESS if status == True else ButtonStyle.DANGER,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_1"],
                callback_data="AUTHLIST",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
                style=ButtonStyle.SUCCESS,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
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
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_11"] if Direct == True else _["ST_B_12"],
                callback_data="MODECHANGE",
                style=ButtonStyle.SUCCESS if Direct == True else ButtonStyle.DANGER,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_13"],
                callback_data="AUTHANSWER",
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_8"] if Group == True else _["ST_B_9"],
                callback_data="CHANNELMODECHANGE",
                style=ButtonStyle.SUCCESS if Group == True else ButtonStyle.DANGER,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["ST_B_14"],
                callback_data="PLAYTYPEANSWER",
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["ST_B_8"] if Playtype == True else _["ST_B_9"],
                callback_data="PLAYTYPECHANGE",
                style=ButtonStyle.SUCCESS if Playtype == True else ButtonStyle.DANGER,
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
                style=ButtonStyle.SUCCESS,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
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
                style=ButtonStyle.SUCCESS if high == True else ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
                style=ButtonStyle.SUCCESS,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
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
                style=ButtonStyle.SUCCESS if high == True else ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
                style=ButtonStyle.SUCCESS,
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
            ),
        ],
    ]
    return buttons
