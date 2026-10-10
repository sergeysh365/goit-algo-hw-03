import random

def get_numbers_ticket(min_value, max_value, quantity):
    '''
    A function that generates a set of unique random numbers for lotteries.

    Input:
    :param min: integer
    :param max: integer
    :param quantity: integer

    Output:
    :return: list
    '''
    if min_value < 1 or max_value > 1000 or quantity < min_value or quantity > max_value: # Перевірка на коректність введених значень
        lottery_numbers = [] # Створення порожнього списку
        print(f'Ваші лотерейні числа: {lottery_numbers}') # Виведення порожнього списку
        return lottery_numbers

    lottery_numbers = sorted(random.sample(range(min_value, max_value + 1), quantity)) # Генерація тільки унікальніх значеннь за допомогою sample
    print(f'Ваші лотерейні числа: {lottery_numbers}')
    return lottery_numbers

if __name__ == '__main__':
    get_numbers_ticket(min_value=1, max_value=49, quantity=6)