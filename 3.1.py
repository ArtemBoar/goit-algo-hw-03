# 1

from datetime import datetime

def get_days_from_today(date):
    ncurrent_date = datetime.strptime(date, '%Y-%m-%d').date()

    today_day = datetime.today().date()

    comparing = today_day - ncurrent_date

    return comparing.days


print(get_days_from_today('2026-10-10'))
