from app.horosopeAPI import HoroscopeAPI


ZODIAC_SIGNS = {
    "Aries": 1,
    "Taurus": 2,
    "Gemini": 3,
    "Cancer": 4,
    "Leo": 5,
    "Virgo": 6,
    "Libra": 7,
    "Scorpio": 8,
    "Sagittarius": 9,
    "Capricorn": 10,
    "Aquarius": 11,
    "Pisces": 12
}


# TODO список знаков по датам на /start
class HoroscopeService:
    def __init__(self, zodiac_sign: str):
        self.zodiac_sign = zodiac_sign
        self.date = None

    def get_zodiac_sign(self):
        return self.zodiac_sign

    def get_zodiac_sign_number(self):
        return ZODIAC_SIGNS.get(self.zodiac_sign)

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def get_horoscope(self):
        greetings = f"Great! That's horoscope for {self.zodiac_sign} for {self.date}"
        return greetings + HoroscopeAPI.get_horoscope_by_day(self.get_zodiac_sign_number(), self.date)

