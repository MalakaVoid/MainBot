from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import CommandStart, Command
from keyboards import start_keyboards

router = Router()

class SupportStates(StatesGroup):


@router.message(CommandStart())
async def start_command(message: Message) -> None:
    """
    START COMMAND HANDLER
    """
    await message.answer("Начало бота",
                         reply_markup=start_keyboards.get_main_menu_kb())


@router.message(F.text == "Поддержка")
async def support_btn(message: Message) -> None:
    """
    ОБРАБОТЧИК КНОПКИ ПОДДЕРЖКИ
    """
    await message.answer("Поддержка",
                         reply_markup=start_keyboards.get_support_menu_kb())

