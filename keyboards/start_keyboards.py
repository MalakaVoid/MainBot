from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, CallbackQuery

def get_main_menu_kb() -> ReplyKeyboardMarkup:
    """
    Default main keyboard
    """
    btn_1 = KeyboardButton(text="Активировать подписку")
    btn_2 = KeyboardButton(text="Поддержка")
    btn_3 = KeyboardButton(text="О компании")

    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[[btn_1], [btn_2, btn_3]]
    )
    return kb

def get_support_menu_kb() -> ReplyKeyboardMarkup:
    """
    Support keyboard
    """
    btn_1 = KeyboardButton(text="Оформить заявку")
    btn_2 = KeyboardButton(text="Назад")

    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[[btn_1, btn_2]]
    )
    return kb

