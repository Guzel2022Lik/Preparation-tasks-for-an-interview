# String / Строковый тип данных

# Задача 2.1. Условие

# Напишите программу, которая удалит переданный символ из строки

def remove_sym(string: str, symbol: str):
    return string.replace(symbol, '')

print(remove_sym('This is my text', ' '))
print(remove_sym('This is my text', 's'))


# Задача 2.2. Условие

# Напишите программу, которая подсчитает количество вхождений подстроки в строку

def count_str(string: str, substring: str):
    return string.count(substring)

print(count_str('This is my text', ' '))
print(count_str('This is my text', 'is'))
