# 31. Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

num = m = int(input("Задайте натуральное число N = "))
divisor = 2
lst = []

while divisor <= num:
    if num % divisor == 0:
        lst.append(divisor)
        num = num // divisor
    else:
        divisor += 1

print(f"Список простых множителей числа {m}: ", lst)
