from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from tgbot.handlers.onboarding.static_text import github_button_text, secret_level_button_text


def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(github_button_text, url="https://github.com/ohld/django-telegram-bot"),
        InlineKeyboardButton(secret_level_button_text, callback_data=f'{SECRET_LEVEL_BUTTON}')
    ]]

    return InlineKeyboardMarkup(buttons)

send_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Telefon raqam", request_contact=True)
        ]
    ],
    resize_keyboard=True,
)
send_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="A'zolikni tekshirish ✅",)
        ]
    ],
    resize_keyboard=True,
)

yes_no = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha ✅",)
        ],
        [
            KeyboardButton(text="Yo'q ❌",)
        ],
    ],
    resize_keyboard=True,
)