# 39. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# конфиг
max_candy = 28
all_candy = 100

win_first = all_candy % (max_candy + 1)
print(f"Для победы первый игрок должен взять в первый ход {win_first} конфет")

player_one_counter = 0
player_two_counter = 0
candy_counter = 0
who_win = 3

while candy_counter <= all_candy:
    print(f'Всего конфет в игре - {all_candy - player_one_counter - player_two_counter}')
    player_one_counter += int(input("Сколько конфет возьмет первый игрок(от 1 до 28): "))
    if player_one_counter + player_two_counter == all_candy:
        who_win = 1
        break
    print(f'Всего конфет в игре - {all_candy - player_one_counter - player_two_counter}')
    p = player_two_counter
    player_two_counter += int(input("Сколько конфет возьмет второй игрок(от 1 до 28): "))
    if player_one_counter + player_two_counter == all_candy:
        who_win = 2
        break
    print(f'Следующим ходом для выигрыша 1-го игрока нужно взять {max_candy + 1 - player_two_counter + p} конфет')
if who_win == 1:
    print('Победил игрок 1')
else:
    print('Победил игрок 2')
