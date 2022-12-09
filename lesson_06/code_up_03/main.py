# 40. Создайте программу для игры в ""Крестики-нолики"".

def list_print(lst):
    for i in range(9):
        print(f"{lst[i]}", end=" ")
        if i == 2 or i == 5 or i == 8:
            print("")


cx = lambda x: True if x == "x" else False
co = lambda y: True if y == "o" else False

def who_win(lst):
    win_list = [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6]]

    for i in win_list:
        if len(list(filter(cx, [lst[i[0]], lst[i[1]], lst[i[2]]]))) == 3:
        # if lst[i[0]] == 'x' and lst[i[1]] == 'x' and lst[i[2]] == 'x':
            return 'x'
        if len(list(filter(co, [lst[i[0]], lst[i[1]], lst[i[2]]]))) == 3:
        # if lst[i[0]] == 'o' and lst[i[1]] == 'o' and lst[i[2]] == 'o':
            return 'o'
    return False


lst = [x for x in range(10)]
list_print(lst)
for i in range(10):
    step = input("Укажите ячейку и х или о через пробел: ").split()
    lst[int(step[0])] = step[1]
    list_print(lst)
    if who_win(lst) != False:
        print(f"Победили {who_win(lst)}")
        break
