from datetime import datetime, timedelta
# import locale
# locale.setlocale(locale.LC_ALL, "ru_RU")
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    dt_now = datetime.now()
    day_ago = dt_now - timedelta(days = 1)
    month_ago = dt_now - timedelta(days = 30)
    print('Вчера: ' + day_ago.strftime('%d.%m.%Y'))
    print('Сегодня: ' + dt_now.strftime('%d.%m.%Y'))
    print('30 назад: ' + month_ago.strftime('%d.%m.%Y'))
    
def str_2_datetime(date_string):
    date_dt = datetime.strptime(date_string, '%y/%m/%d %H:%M:%S.%f')
    print('Добавленная дата: ' + date_dt.strftime('%d/%m/%Y %H:%M'))

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
