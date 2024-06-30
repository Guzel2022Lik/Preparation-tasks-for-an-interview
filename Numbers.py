# 1.1 Напишите программу, которая развернет число (тип int)

def revert_int_option_1(num):
    print('Option 1: Use reversed() method')
    return int(''.join(list(reversed(str(num)))))


def revert_int_option_2(num):
    print('Option 2: Use slices')
    return int(str(num)[::-1])


print(revert_int_option_1(12345))
print(revert_int_option_2(12345))


# 1.2 Напишите программу, которая проверяет, является ли число числом Армстронга. 
# Число Армстронга — натуральное число, которое в данной системе счисления равно сумме своих цифр, возведённых в степень, равную количеству его цифр.

def armstrong_number(num):
    sum = 0
    length = len(str(num))
    for digit in list(str(num)):
        sum += int(digit)**length
    return sum == num

print(armstrong_number(371))


# 1.3 Напишите программу, которая проверит каждое число в списке на предмет того, является ли оно простым.

def prime_num(num):
    for div_num in range(2, num):
        if num % div_num == 0:
            return False
    return True

for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
    print(f"{item}: {prime_num(item)}")


# 1.4 Напишите программу, которая построит список чисел Фибоначчи через итеративный метод.


def fibonacci(length):
    lst = [0, 1]
    for item, index in enumerate(range(2, length)):
        lst.append(lst[index-2] + lst[index-1])
    return lst

print(fibonacci(14))


# 1.5 Напишите программу, которая построит список чисел Фибоначчи через рекурсию. 
#     Числа Фибоначчи - элементы числовой последовательности, в которой первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел.

def fibonacci(length):
    lst = [0, 1]
    return calculate_next(lst, length)

def calculate_next(lst, length):
    if len(lst) < length:
        lst.append(lst[-2] + lst[-1])
        return calculate_next(lst, length)
    else:
        return lst

print(fibonacci(14))


# 1.6 Напишите программу, которая посчитает факториал от заданного числа (через рекурсию).

def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x-1)

print(factorial(5))


# 1.7 Напишите программу, которая проверит, является ли число палиндромом.

def prime_num(num):
    for div_num in range(2, num):
        if num % div_num == 0:
            return False
    return True

for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
    print(f"{item}: {prime_num(item)}")


# 1.8 Напишите программу, которая проверит, является ли число палиндромом (итеративным способом).

def is_palindrome(num):
    str_num = str(num)
    median = len(str_num)//2
    for index in range(0, median):
        if str_num[index] != str_num[len(str_num)-index-1]:
            return False
    return True

print(is_palindrome(54321))
print(is_palindrome(543821))
print(is_palindrome(5346435))
print(is_palindrome(53466435))


# 1.9 Напишите программу, которая проверит, является ли число палиндромом (через рекурсию).

def is_palindrome(num):
    str_num = str(num)
    median = len(str_num)//2
    return check_equalness(str_num, 0, median)

def check_equalness(num, index, median):
    if index >= median:
        return True
    else:
        if num[index] != num[len(num)-index-1]:
            return False
        return check_equalness(num, index+1, median)

print(is_palindrome(54321))
print(is_palindrome(543821))
print(is_palindrome(5346435))
print(is_palindrome(53466435))
