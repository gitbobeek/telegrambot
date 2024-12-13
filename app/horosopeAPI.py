import requests
from bs4 import BeautifulSoup

class HoroscopeAPI:
    @staticmethod
    def get_horoscope_by_day(zodiac_sign: int, day: str) -> str:
        if not "-" in day:
            res = requests.get(f"c")
        else:
            # Дата указывается как ГГГГ-ММ-ДД
            day = day.replace("-", "")
            res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}")
        
        soup = BeautifulSoup(res.content, 'html.parser')
        data = soup.find('div', attrs={'class': 'main-horoscope'})
        return data.p.text if data else "Гороскоп не найден."
    