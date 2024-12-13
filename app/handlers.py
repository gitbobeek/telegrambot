from aiogram import F, Router, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb
from app.horoscope_service import ZODIAC_SIGNS
from app.horoscope_service import HoroscopeService

class RouterHandler:
    def __init__(self, dp: Dispatcher):
        self.router = Router()
        self.dp = dp
        self.register_handlers()
        self.get_horoscope()

    def register_handlers(self):
        @self.router.message(CommandStart())
        async def cmd_start(message: Message):
            await message.answer('Добро пожаловать в наш мир гороскопов.', reply_markup=kb.main)


        @self.router.message(Command('help'))
        async def cmd_help(message: Message):
            await message.answer('Здравствуйте! Вы обратились к /help')

    
    def get_horoscope(self):    
        @self.router.message(F.text == 'Узнать гороскоп')
        async def msg_epta(message: Message):
            await message.answer('Укажите знак зодиака', reply_markup=kb.zodiac_keyboard)


        @self.router.callback_query(F.data == 'date')
        async def today_horoscope(callback: CallbackQuery):
            await callback.message.answer('Итак, рассмотрим гороскоп на сегодня...')

       # @self.router.message()

        self.dp.include_router(self.router)
