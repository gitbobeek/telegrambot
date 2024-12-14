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
    
    @staticmethod
    def show_signs():
        return("Aries (March 21 – April 19)\n"+
               "Taurus (April 20 – May 20)\n"+ 
               "Gemini (May 21 – June 20)\n"+
               "Cancer (June 21 – July 22)\n"+
               "Leo (July 23 – August 22)\n"+
               "Virgo (August 23 – September 22)\n"+
                "Libra (September 23 – October 22)\n" +
                "Scorpio (October 23 – November 21)\n"+
                "Sagittarius (November 22 – December 21)\n"+
                "Capricorn (December 22 – January 19)\n"+
                "Aquarius (January 20 – February 18)\n"+
                "Pisces (February 19 – March 20)\n")

    def get_horoscope(self):
        greetings = f"Great! Here is the horoscope for {self.zodiac_sign} for {self.date}\n"
        return greetings + HoroscopeAPI.get_horoscope_by_day(self.get_zodiac_sign_number(), self.date)

