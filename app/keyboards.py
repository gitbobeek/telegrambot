from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Узнать гороскоп')],
                                     [KeyboardButton(text='Настроить сообщения от бота')],
                                     [KeyboardButton(text='В начало')]],
                           resize_keyboard=True,
                           input_field_placeholder='Ожидание ответа...')

date_choose = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гороскоп на сегодня', callback_data='today')],
    [InlineKeyboardButton(text='Гороскоп на завтра', callback_data='tomorrow')],
    [InlineKeyboardButton(text='Выбрать дату...', callback_data='date')]])

zodiac_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Овен', callback_data='Aries')],
    [InlineKeyboardButton(text='Телец', callback_data='Taurus')],
    [InlineKeyboardButton(text='Близнецы', callback_data='Gemini')],
    [InlineKeyboardButton(text='Рак', callback_data='Cancer')],
    [InlineKeyboardButton(text='Лев', callback_data='Leo')],
    [InlineKeyboardButton(text='Дева', callback_data='Virgo')],
    [InlineKeyboardButton(text='Весы', callback_data='Libra')],
    [InlineKeyboardButton(text='Скорпион', callback_data='Scorpio')],
    [InlineKeyboardButton(text='Стрелец', callback_data='Sagittarius')],
    [InlineKeyboardButton(text='Козерог', callback_data='Capricorn')],
    [InlineKeyboardButton(text='Водолей', callback_data='Aquarius')],
    [InlineKeyboardButton(text='Рыбы', callback_data='Pisces')]])
