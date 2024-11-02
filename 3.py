from datetime import datetime

"1"
def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        today_date = datetime.today().date()
        delt = given_date - today_date
        return delt.days
    except ValueError:
        return print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")


print(get_days_from_today("2021-10-09"))

from datetime import datetime


"2"

import random

def get_numbers_ticket(min: int,max: int, qntity):
    if min < 1 or max > 1000 or qntity > max - min + 1:
        return []
    return sorted(random.sample(range(min, max + 1), qntity))


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші  лотерейні  числа:", lottery_numbers)


"3"

import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    if cleaned_number.startswith('380'):
        cleaned_number = '+' + cleaned_number
    elif not cleaned_number.startswith('+'):
        cleaned_number = '+38' + cleaned_number
    return cleaned_number

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)