# 18. Реализуйте алгоритм перемешивания списка.

import random

lst = list(range(1, 11))
print("Исходный список: ", lst)
# Первый способ:
# random.shuffle(lst)

# Второй способ / что бы ни одна позиция не сохранила свое положение:
new_lst = []
index_lst = []
for i in range(len(lst)):
    while True:
        c = random.randint(0, len(lst) - 1)
        if c != i and c not in index_lst:
            index_lst.append(c)
            new_lst.append(lst[c])
            break
lst = new_lst

print("Список после перемешивания: ", lst)

