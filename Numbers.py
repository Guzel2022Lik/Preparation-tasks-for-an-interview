# 1.1 Напишите программу, которая развернет число (тип int)

def revert_int_option_1(num):
    print('Option 1: Use reversed() method')
    return int(''.join(list(reversed(str(num)))))


def revert_int_option_2(num):
    print('Option 2: Use slices')
    return int(str(num)[::-1])


print(revert_int_option_1(12345))
print(revert_int_option_2(12345))
