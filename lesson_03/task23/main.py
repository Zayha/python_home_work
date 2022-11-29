# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def check_parity(num: int):
    """
    Проверка четности
    :param num: число которое будет проверено
    :return: True - если четное, False - если нет
    """
    if num % 2 == 0:
        return True
    else:
        return False


result = []
lst = list(map(int, input("Введите список из чисел, разделяя их запятой: ").split(",")))
for i in range(0, len(lst) // 2):
    result.append(lst[i] * lst[len(lst) - 1 - i])
if not check_parity(len(lst)):
    result.append(lst[len(lst) // 2] ** 2)
print(lst, " => ", result)
