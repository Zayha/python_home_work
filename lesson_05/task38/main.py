# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# # 1-ый вариант
# def find_target():
#     target = 'абв'
#     if target in pcs :
#         return False
#     else:
#         return True
#
#
# result = list(filter(find_target, input("Введите, что-то эдакое: ").split()))
# print(result)

# 2-й вариант

print(" ".join(list(filter(lambda x: False if 'абв' in x else True, input("Введите, что-то эдакое: ").split()))))
