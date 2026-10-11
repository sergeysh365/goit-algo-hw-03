import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
	"+442079460915",
    " +  (4930123456)",
    '+33-123-45-67-89',
    "+8613800138000",
    "(81) 901 23 45 678"
]

def normalize_phone(phone_number: str) -> str:
    '''
    A function that normalizes phone numbers to a standard format +380XXXXXXXXX.

    Input:
    :param phone_number: string

    Output:
    :return: string
    '''
    cleaned = re.sub(r'[^\+\d]', '', phone_number) # Видалення всіх знаків, окрім '+' і цифр
    if cleaned.startswith('+'):
        pass # Залишаємо номер без змін, якщо він починається з '+'
    elif cleaned.startswith('380'):
        cleaned = '+' + cleaned #  Додаємо '+' на початок номера, якщо він починається з '380'
    elif cleaned.startswith('0'):
        cleaned = '+38' +  cleaned # Додаємо '+38' на початок номера, якщо він починається з '0'
    else:
        cleaned = '+' + cleaned # Додаємо '+' на початок номера, якщо він не починається з '+', '380' або '0'
    return cleaned # Повертаємо результат у вигляді рядка з одного номера
    
sanitized_numbers = [] # Створення порожнього списку для зберігання всіх номерів у нормалізованому форматі

for phone in raw_numbers: # Проходження по оригінальному списку
    sanitized_numbers.append(normalize_phone(phone))  # Додаємо номери у нормалізованому форматі до списку 
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)