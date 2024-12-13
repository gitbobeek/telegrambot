import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import RouterHandler
from config import TOKEN

class HoroscopeBot:
    def __init__(self, token: str):
        self.bot = Bot(token=TOKEN)
        self.dp = Dispatcher()
        self.router_handler = RouterHandler(self.dp)

    async def start(self):
        await self.dp.start_polling(self.bot)

if __name__ == '__main__':
    try:
        bot = HoroscopeBot(token=TOKEN)
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        print('Бот выключен')
