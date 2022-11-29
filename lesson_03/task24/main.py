# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

remainder_of_division = []
lst = list(map(float, input("Введите список из чисел, разделяя их запятой: ").split(",")))
for i in lst:
    if i % 1 != 0:
        remainder_of_division.append(i % 1)

num_max, num_min = (max(remainder_of_division), min(remainder_of_division))
result = num_max - num_min
print(f"=> {result:.2f}")
