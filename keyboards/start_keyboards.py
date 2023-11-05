from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import KeyboardBuilder

def get_main_menu_kb() -> ReplyKeyboardMarkup:
    """
    ГЛАВНОЕ МЕНЮ
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
    ПОДДЕРЖКА
    """
    btn_1 = KeyboardButton(text="Оформить заявку")
    btn_2 = KeyboardButton(text="Назад")

    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[[btn_1, btn_2]]
    )
    return kb


def get_about_company_kb() -> ReplyKeyboardMarkup:
    """
    О КОМПАНИИ
    """
    btn_1 = KeyboardButton(text="Основная информация")
    btn_2 = KeyboardButton(text="Сервисы")

    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[[btn_1, btn_2]]
    )
    return kb


def get_about_company_main_info() -> ReplyKeyboardMarkup:
    """
    О КОМПАНИИ - ОСНОВНАЯ ИНФОРМАЦИЯ -

    --ПРИВЕЛЕГИИ--
    """
    btn_1 = KeyboardButton(text="Привелегии")
    btn_2 = KeyboardButton(text="Главное меню")

    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[[btn_1], [btn_2]]
    )
    return kb


def get_about_compony_services() -> ReplyKeyboardMarkup:
    """
    О КОМПАНИИ - СЕРВИСЫ

    --все сервисы--
    """
    btn_1 = KeyboardButton(text="S1")
    btn_2 = KeyboardButton(text="S2")
    btn_3 = KeyboardButton(text="S3")
    btn_4 = KeyboardButton(text="Главное меню")

    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[[btn_1],[btn_2],[btn_3],[btn_4]]
    )
    return kb


def get_only_main_menu_btn() -> ReplyKeyboardMarkup:
    """
    ТОЛЬКО КНОПКА ВОЗВРАТА В ГЛАВНОЕ МЕНЮ
    ENDPOINT
    """
    btn_1 = KeyboardButton(text="Главное меню")

    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[[btn_1]]
    )
    return kb


def get_activation_subscribe_privileges() -> ReplyKeyboardMarkup:
    """
    Активировать подписку

    --Привилегии--
    !!!ПОКА ЧТО ИЗ МАССИВА ВНУТРИ ФУНКЦИИ - privileges
    !!!!! ОТКУДА БРАТЬ ПРИВИЛЕГИИ ИЗ БД ИЛИ ВРУЧНУЮ ИХ ВПИХНУТЬ
    """
    privileges = ["Привилегия 1", "Привилегия 2"]
    builder = KeyboardBuilder(button_type=KeyboardButton)
    for privilege in privileges:
        builder.add(KeyboardButton(text=privilege))

    builder.adjust(1, 2)
    return builder.as_markup(resize_keyboard=True)


