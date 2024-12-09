from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Узнать гороскоп')],
                                     [KeyboardButton(text='Настроить сообщения от бота')], 
                                     [KeyboardButton(text='В начало')]], 
                          resize_keyboard=True, 
                          input_field_placeholder='Выберите ответ по кнопке ниже...')


date = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гороскоп на сегодня', callback_data='today-horoscope')],
    [InlineKeyboardButton(text='Гороскоп на завтра', callback_data='tomorrow-horoscope')],
    [InlineKeyboardButton(text='Выбрать дату...', callback_data='date-horoscope')]])
