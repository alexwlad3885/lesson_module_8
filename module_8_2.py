# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции".
def personal_sum(numbers):
    result: int = 0
    incorrect_data: int = 0
    i: int
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_data


def calculate_average(numbers):
    elem_tuple: tuple
    elem_sum: int
    elem_quantity: int
    try:
        elem_tuple = personal_sum(numbers)
        elem_sum = elem_tuple[0]
        elem_quantity = len(numbers) - elem_tuple[1]
        return elem_sum / elem_quantity
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
