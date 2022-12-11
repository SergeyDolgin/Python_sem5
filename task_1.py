# На выбор
# 1. Создайте программу для игры с конфетами человек против человека.
# ' Условие задачи На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

import random
candy = 117

def move_user():
    global candy
    while True:
        move = int(input('Введите количество конфет '))
        if move > 0 and move < 29 and move <= candy:
            candy = candy-move
            break
        else:
            print('Нельзя взять такое количесто конфет')

def move_bot():
    global candy
    while True:
        move = random.randint(1,28)
        if move <= candy:
            print(f'Бот взял {move}')
            candy = candy-move
            break






print(f'На столе лежит {candy} конфет')
players = ['user', 'bot']
move = random.choice(players)
print(f'Первым ходит {move}')
while True:
    if move == 'user':
        move_user()
        print(f'Осталось {candy}')
        move = 'bot'
        if candy < 29:
            print(f'Победил {move}')
            break
    else:
        move_bot()
        print(f'Осталось {candy}')
        move = 'user'
        if candy < 29:
            print(f'Победил {move}')
            break    
