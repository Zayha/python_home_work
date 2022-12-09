# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# #
# # Пример:
# #
# # - 6782 -> 23
# # - 0,56 -> 11
#
# num = float(input("Введите число: "))
# st = str(num).replace(".", "", 1).replace("0", "")
# result = 0
# for i in st:
#     result += int(i)
# print(f"{num} -> {result}")

print(sum(list(map(int, str(float(input("Введите число: "))).replace(".", "", 1).replace("0", "")))))