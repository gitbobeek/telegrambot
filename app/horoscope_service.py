
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
# TODO список знаков по датам на  /start
class HoroscopeService:
    def __init__(self, zodiac_sign):
        self.zodiac_sign = get_zodiac_sign()
    
    def get_zodiac_sign(self):
        return self.zodiac_sign()