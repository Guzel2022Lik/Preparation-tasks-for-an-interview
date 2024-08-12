# String / Строковый тип данных

# Задача 2.1. Условие

# Напишите программу, которая удалит переданный символ из строки

def remove_sym(string: str, symbol: str):
    return string.replace(symbol, '')

print(remove_sym('This is my text', ' '))
print(remove_sym('This is my text', 's'))
