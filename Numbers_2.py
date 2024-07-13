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
