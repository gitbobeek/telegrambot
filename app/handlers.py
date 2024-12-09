from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в наш епта мир гороскопов.', reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Здравствуйте! Вы обратились к /help')


@router.message(F.text == 'Узнать гороскоп')
async def msg_epta(message: Message):
    await message.answer('Давайте узнаем', reply_markup=kb.date)


@router.callback_query(F.data == 'today-horoscope')
async def today_horoscope(callback: CallbackQuery):
    await callback.message.answer('Итак, рассмотрим гороскоп на сегодня...')