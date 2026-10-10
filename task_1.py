from datetime import datetime

def get_days_from_today(date: str) -> int: # Функція розраховує кількість днів між заданою датою і поточною датою
    '''
    A function to calculate the number of days between a given date and the current date.

    Input:
    :param date: string

    Output:
    :return: integer
    '''
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date() # Перетворення рядка у дату
    except ValueError:
        print('Введіть дату у форматі: РРРР-ММ-ДД')
    else:
        current_date = datetime.today().date() # Отримання поточної дати
        diff_days = date - current_date
        print(diff_days.days)
        return diff_days.days

get_days_from_today('2029-10-05')