# 1.12 Напишите программу, которая принимает на вход число и раскладывает его на простые множители. 
# Разложить на простые множители — значит представить число в виде произведения простых множителей (чисел). 
# Простые множители вернуть в виде списка.

def factorize(num):
    left_portion = num
    factors = []
    index = 2
    while left_portion != 1:
        while left_portion % index == 0:
            factors.append(index)
            left_portion = left_portion / index
        index += 1

    return factors

print(factorize(5))
print(factorize(52))
print(factorize(63))


# Напишите программу, которая проверит, что число является совершенным. 
# Совершенное число - натуральное число, равное сумме всех своих собственных делителей. 
# Например, число 6 равно сумме своих собственных делителей 1 + 2 + 3. 
# Примеры совершенных чисел: 6, 28, 496, 8128


def get_divisors(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return divisors

def perfect_num(num):
    divisors = get_divisors(num)
    return num == sum(divisors)

print(perfect_num(6))
print(perfect_num(28))
print(perfect_num(496))
print(perfect_num(8128))


# 1.14
# Напишите программу, которая найдет среднее арифметическое списка чисел

def average(lst):
    return sum(lst) / len(lst)

print(average([1, 5, 10, 35, 234, 1, 6, 8]))

# 1.15 Напишите программу, которая выведет первые N простых чисел

def simple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = 10
simple_numbers = [1]
index = 1
while len(simple_numbers) < 10:
    index += 1
    if simple(index):
        simple_numbers.append(index)

print(simple_numbers)


# 1.16 Напишите программу, которая выведет простые числа в заданном диапазоне


def simple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

start = 5
end = 50
simple_numbers = [1] if start == 1 else []
index = start
for index in range(start, end):
    if simple(index):
        simple_numbers.append(index)

print(simple_numbers)


# 1.17
# Напишите программу, которая найдет наименьшее общее кратное двух чисел. 
# Наименьшее общее кратное двух чисел - это наименьшее натуральное число, которое делится без остатка на оба числа.

def less_comm_multiple(a, b):
    index = 2
    while True:
        if index % a == 0 and index % b == 0:
            return index
        index += 1

print(less_comm_multiple(5, 7))
print(less_comm_multiple(10, 3))
