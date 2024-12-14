from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Get my horoscope')],
                                     [KeyboardButton(text="What's my sign?")]],
                           resize_keyboard=True,
                           input_field_placeholder='Await...')

date_choose = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='For today', callback_data='today')],
    [InlineKeyboardButton(text='For tomorrow', callback_data='tomorrow')],
    [InlineKeyboardButton(text='Choose date...', callback_data='date')]])

zodiac_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='♈ Aries', callback_data='Aries')],
    [InlineKeyboardButton(text='♉ Taurus', callback_data='Taurus')],
    [InlineKeyboardButton(text='♊ Gemini', callback_data='Gemini')],
    [InlineKeyboardButton(text='♋ Cancer', callback_data='Cancer')],
    [InlineKeyboardButton(text='♌ Leo', callback_data='Leo')],
    [InlineKeyboardButton(text='♍ Virgo', callback_data='Virgo')],
    [InlineKeyboardButton(text='♎ Libra', callback_data='Libra')],
    [InlineKeyboardButton(text='♏ Scorpius', callback_data='Scorpio')],
    [InlineKeyboardButton(text='♐ Sagittarius', callback_data='Sagittarius')],
    [InlineKeyboardButton(text='♑ Capricornus', callback_data='Capricorn')],
    [InlineKeyboardButton(text='♒ Aquarius', callback_data='Aquarius')],
    [InlineKeyboardButton(text='♓ Pisces', callback_data='Pisces')]])
