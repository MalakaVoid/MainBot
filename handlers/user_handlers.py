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
    """
    СОСТОЯНИЯ ДЛЯ ВЕТКИ ПОДДЕРЖКА
    """
    startSupport = State()
    makeRequest = State()


class AboutCompanyStates(StatesGroup):
    """
    СОСТОЯНИЯ ДЛЯ ВЕТКИ О КОМПАНИИ
    """
    start = State()
    mainInfo = State()
    services = State()


class ActivateSubState(StatesGroup):
    """
    СОСТОЯНИЯ ДЛЯ ВЕТКИ АКТИВАЦИЯ ПОДПИСКИ
    """
    privilege = State()
    pay = State()


@router.message(CommandStart())
async def start_command(message: Message) -> None:
    """
    START COMMAND HANDLER
    """
    await message.answer("Главное меню",
                         reply_markup=start_keyboards.get_main_menu_kb())


@router.message(F.text == "Главное меню")
async def go_to_main_menu_btn(message: Message, state: FSMContext):
    """
    ОТПРАВКА В ГЛАВНОЕ МЕНЮ ИЗ ЛЮБОЙ ТОЧКИ
    """
    await state.clear()
    await message.answer("Главное меню",
                         reply_markup=start_keyboards.get_main_menu_kb())


@router.message(F.text == "Поддержка")
async def support_btn(message: Message, state: FSMContext) -> None:
    """
    ОБРАБОТЧИК КНОПКИ ПОДДЕРЖКИ
    """
    await state.set_state(SupportStates.startSupport)
    await message.answer("Поддержка",
                         reply_markup=start_keyboards.get_support_menu_kb())


@router.message(SupportStates.startSupport, F.text == "Назад")
async def back_from_support_btn(message: Message, state: FSMContext) -> None:
    """
    ОБРАБОТЧИК КНОПКИ НАЗАД ИЗ ПОДДЕРЖКИ
    """
    await message.answer("Главное меню",
                         reply_markup=start_keyboards.get_main_menu_kb())
    await state.clear()


@router.message(SupportStates.startSupport, F.text == "Назад")
async def make_request_to_support_btn(message: Message, state: FSMContext) -> None:
    """
    ОБРАБОТЧИК КНОПКИ ОФОРМИТЬ ЗАЯВКУ В ПОДДЕРЖКУ
    """
    await message.answer("Оформить заявку",
                         reply_markup=None)
    await state.set_state(SupportStates.makeRequest)


@router.message(F.text == "О компании")
async def about_company_btn(message: Message, state: FSMContext) -> None:
    """
    ОБРАБОТЧИК КНОПКИ О КОМПАНИИ
    """
    await state.set_state(AboutCompanyStates.start)
    await message.answer("О компании",
                         reply_markup=start_keyboards.get_about_company_kb())


@router.message(AboutCompanyStates.start, F.text == "Основная информация")
async def main_info_about_company_btn(message: Message, state: FSMContext) -> None:
    """
    ОБРАБОТЧИК КНОПКИ ОСНОВАНЯ ИНФОРМАЦИЯ О КОМПАНИИ
    """
    await state.set_state(AboutCompanyStates.mainInfo)
    await message.answer("Основная информация",
                         reply_markup=start_keyboards.get_about_company_main_info())


@router.message(AboutCompanyStates.mainInfo, F.text == "Привелегии")
async def main_info_about_company_privelegies_btn(message: Message, state: FSMContext) -> None:
    """
    ОБРАБОТЧИК КНОПКИ ПРИВЕЛЕГИИ В ОСНОВНОЙ ИНФОРМАЦИИ О КОМПАНИИ
    """
    await message.answer("Привелегии",
                         reply_markup=start_keyboards.get_only_main_menu_btn())


@router.message(AboutCompanyStates.start, F.text == "Сервисы")
async def about_company_services_btn(message: Message, state: FSMContext) -> None:
    """
    ОБРАБОТЧИК КНОПКИ СЕРВИСЫ ИЗ О КОМПАНИИ
    """
    await state.set_state(AboutCompanyStates.services)
    await message.answer("Сервисы",
                         reply_markup=start_keyboards.get_about_compony_services())


@router.message(F.text == "Активировать подписку")
async def activate_subscription_btn(message: Message, state: FSMContext) -> None:
    """
    ОБРАБОТЧИК КНОПКИ АКТИВИРОВАТЬ ПОДПИСКУ
    """
    await state.set_state(ActivateSubState.privilege)
    await message.answer("Активировать подписку\nВыберите привилегию.",
                         reply_markup=start_keyboards.get_activation_subscribe_privileges())


@router.message(ActivateSubState.privilege, F.text == "Привилегия 1")
async def privilege_one_btn(message: Message, state: FSMContext) -> None:
    """
    ОБРАБОТЧИК КНОПКИ ПРИВИЛЕГИИ 1 В АКТИВАЦИИ ПОДПИСКИ
    """
    await state.set_state(state=ActivateSubState.pay)
    await state.set_data({"privilege": 1})
    await message.answer("Привилегия 1",
                         reply_markup=start_keyboards.get_activation_subscribe_privileges_cur())


@router.message(ActivateSubState.privilege, F.text == "Привилегия 2")
async def privilege_two_btn(message: Message, state: FSMContext) -> None:
    """
    ОБРАБОТЧИК КНОПКИ ПРИВИЛЕГИИ 2 В АКТИВАЦИИ ПОДПИСКИ
    """
    await state.set_state(state=ActivateSubState.pay)
    await state.set_data({"privilege": 2})
    await message.answer("Привилегия 2",
                         reply_markup=start_keyboards.get_activation_subscribe_privileges_cur())


@router.message(ActivateSubState.pay, F.text == "Оплата")
async def payment_btn(message: Message, state: FSMContext) -> None:
    """
    ОБРАБОТЧИК КНОПКИ ОПЛАТЫ ПОСЛЕ ВЫБОРА ПРИВИЛЕГИИ
    """
    data = await state.get_data()
    print(data)

    await state.clear()
    await message.answer(f"Оплата привелегии {data['privilege']}")
    await message.answer("Главное меню",
                         reply_markup=start_keyboards.get_main_menu_kb())


@router.message(ActivateSubState.pay, F.text == "Назад")
async def back_from_pay_btn(message: Message, state: FSMContext) -> None:
    """
    ОБРАБОТЧИК КНЛППКИ НАЗАД ИЗ ОПЛАТЫ
    """
    await state.set_state(ActivateSubState.privilege)
    await message.answer("Активировать подписку\nВыберите привилегию.",
                         reply_markup=start_keyboards.get_activation_subscribe_privileges())