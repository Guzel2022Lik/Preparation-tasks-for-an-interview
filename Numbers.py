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
