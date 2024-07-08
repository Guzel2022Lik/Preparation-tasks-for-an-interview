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
