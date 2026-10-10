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
]

def normalize_phone(phone_number: str) -> list[str]:
    '''
    A function that normalizes phone numbers to a standard format +380XXXXXXXXX.

    Input:
    :param phone_number: string

    Output:
    :return: list
    '''
    cleaned = re.sub(r'\D', '', phone_number) # Очищення номеру від будь-яких знаків і символів
    if cleaned.startswith('380'):
        cleaned = '+' + cleaned # Додавання префіксу '+' до номера який починається з '380'
    else:
        cleaned = '+38' + cleaned # Додавання префіксу +38 до номера який не починається з '380'
    return [cleaned] # Повертаємо результат у вигляді списку з одного елемента

if __name__ == '__main__':
    sanitized_numbers = [] # Створення порожнього списку для зберігання всіх елементів списку


    for phone in raw_numbers: # Проходження по оригінальному списку
        sanitized_numbers.extend(normalize_phone(phone))  # Оскільки функція повертає СПИСОК, додаємо його елементи через .extend()
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)