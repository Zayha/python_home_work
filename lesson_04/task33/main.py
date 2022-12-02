# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def get_random_list(k, start_n=0, stop_n=100):
    lst = []
    while k + 1 > 0:
        lst.append(random.randint(start_n, stop_n))
        k -= 1
    return lst


k = int(input("Укажите степень k = "))
lst_k = get_random_list(k)

with open("result.txt", "w") as f:
    for i in range(0, k + 1):
        if i < k - 1 and lst_k[i] > 0:
            string_line = f"{lst_k[i]}*x^{k - i} + "
            f.write(string_line)
        elif k - 1 == i and lst_k[i] > 0:
            string_line = f"{lst_k[i]}*x + "
            f.write(string_line)
        else:
            string_line = f"{lst_k[i] if lst_k[i] > 0 else ''} = 0"
            f.write(string_line)
with open("result.txt") as f:
    print(f.read())
