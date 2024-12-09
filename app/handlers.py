from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

class RouterHandler:
    def __init__(self, dispatcher: Router):
        self.router = Router()
        self.setup_routes(dispatcher)

    def setup_routes(self, dispatcher: Router):
        dispatcher.include_router(self.router)
        self.router.message(CommandStart())(self.cmd_start)
        self.router.message(Command('help'))(self.cmd_help)
        self.router.message(F.text == 'Узнать гороскоп')(self.msg_epta)
        self.router.callback_query(F.data == 'today-horoscope')(self.today_horoscope)

    async def cmd_start(self, message: Message):
        await message.answer('Добро пожаловать в наш епта мир гороскопов.', reply_markup=kb.main)

    async def cmd_help(self, message: Message):
        await message.answer('Здравствуйте! Вы обратились к /help')

    async def msg_epta(self, message: Message):
        await message.answer('Давайте узнаем', reply_markup=kb.date)

    async def today_horoscope(self, callback: CallbackQuery):
        await callback.message.answer('Итак, рассмотрим гороскоп на сегодня...')