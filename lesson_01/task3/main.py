# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x, y = map(float, input('Введите x, y через запятую, прим. (-5.3, 7) : ').split(','))
if x != 0 or y != 0:
    if x > 0 and y > 0:
        print(f"x = {x}, y = {y} -> 1")
    if x > 0 and y < 0:
        print(f"x = {x}, y = {y} -> 2")
    if x < 0 and y < 0:
        print(f"x = {x}, y = {y} -> 3")
    if x < 0 and y > 0:
        print(f"x = {x}, y = {y} -> 4")