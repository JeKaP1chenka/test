from aiogram import types
from aiogram.types import InlineKeyboardButton as IKB

board = types.InlineKeyboardMarkup(
    inline_keyboard=[
        # 1 слой 3 кнопки
        [
            IKB(text="", callback_data=""),
            IKB(text="", callback_data=""),
            IKB(text="", callback_data=""),
        ],
        # 2 слой 3 кнопки
        [
            IKB(text="", callback_data=""),
            IKB(text="", callback_data=""),
            IKB(text="", callback_data=""),
        ],
        # 3 слой 3 кнопки
        [
            IKB(text="", callback_data=""),
            IKB(text="", callback_data=""),
            IKB(text="", callback_data=""),
        ]
    ]
)