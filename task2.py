# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
# - 6 -> [2,3]
# - 144 -> [2,3]

num = int(input('Введите число N: '))
multi = [1]
div = 2
while num > 1:
    if num % div == 0:
        num /= div
        if div not in multi:
            multi.append(div)
        div = 2
    else:
        div += 1

print(multi)