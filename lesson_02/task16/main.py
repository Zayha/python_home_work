# 16. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9,06

num = int(input("Введите число n: "))
res_line = []
res_dict = {}
for i in range(1, num + 1):
    calc = round((1 + 1 / i) ** i, 2)
    res_line.append(calc)
    res_dict[i] = calc
result = sum(res_line)
print(res_line, f" Сумма = {result}")
print(res_dict, f" Сумма = {result}")
