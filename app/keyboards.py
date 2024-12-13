from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Узнать гороскоп')],
                                     [KeyboardButton(text='Настроить сообщения от бота')], 
                                     [KeyboardButton(text='В начало')]], 
                          resize_keyboard=True, 
                          input_field_placeholder='Ожидание ответа...')


date_choose = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гороскоп на сегодня', callback_data='date')],
    [InlineKeyboardButton(text='Гороскоп на завтра', callback_data='date')],
    [InlineKeyboardButton(text='Выбрать дату...', callback_data='date')]])


zodiac_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Овен', callback_data='ARIES')],
    [InlineKeyboardButton(text='Телец', callback_data='TAURUS')],
    [InlineKeyboardButton(text='Близнецы', callback_data='GEMINI')],
    [InlineKeyboardButton(text='Рак', callback_data='CANCER')],
    [InlineKeyboardButton(text='Лев', callback_data='LEO')],
    [InlineKeyboardButton(text='Дева', callback_data='VIRGO')],
    [InlineKeyboardButton(text='Весы', callback_data='LIBRA')],
    [InlineKeyboardButton(text='Скорпион', callback_data='SCORPIO')],
    [InlineKeyboardButton(text='Стрелец', callback_data='SAGITTARIUS')],
    [InlineKeyboardButton(text='Козерог', callback_data='CAPRICORN')],
    [InlineKeyboardButton(text='Водолей', callback_data='AQUARIUS')],
    [InlineKeyboardButton(text='Рыбы', callback_data='PISCES')]])
