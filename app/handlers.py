from aiogram import F, Router, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb
from app.horoscope_service import ZODIAC_SIGNS, HoroscopeService


class RouterHandler:
    def __init__(self, dp: Dispatcher):
        self.router = Router()
        self.dp = dp
        self.start_handlers()
        self.current_service = None

    def start_handlers(self):
        @self.router.message(CommandStart())
        async def cmd_start(message: Message):
            await message.answer('Welcome to !',
                                 reply_markup=kb.main)
            
        @self.router.message(F.text == "What's my sign?")
        async def msg_show_signs(message: Message):
            await message.answer(HoroscopeService.show_signs())

        # @self.router.message(Command('help'))
        # async def cmd_help(message: Message):
        #     await message.answer('Здравствуйте! Вы обратились к /help')

        @self.router.message(F.text == 'Get my horoscope')
        async def msg_send_sign_pls(message: Message):
            await message.answer('Pick your sign',
                                 reply_markup=kb.zodiac_keyboard)

        @self.router.callback_query(F.data.in_(ZODIAC_SIGNS.keys()))
        async def set_zodiac_sign(callback: CallbackQuery):
            self.current_service = HoroscopeService(callback.data)
            await callback.message.answer('Thank you. Now let me know, for what day do u want to see horoscope',
                                          reply_markup=kb.date_choose)

        @self.router.callback_query(F.data.in_({'today', 'tomorrow'}))
        async def msg_show_horoscope_easy(callback: CallbackQuery):
            self.current_service.set_date(callback.data)
            await callback.message.answer(self.current_service.get_horoscope())

        @self.router.callback_query(F.data == 'date')
        async def msg_show_horoscope_for_exact_date(callback: CallbackQuery):
            await callback.message.answer('Please enter the date with YYYY-MM-DD format.')

            @self.router.message(F.text)
            async def msg_get_date(message: Message):
                date_input = message.text
                self.current_service.set_date(date_input)

                await callback.message.answer(self.current_service.get_horoscope())

        self.dp.include_router(self.router)
