from random import *
import os


welcome_text = ('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n'
                'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \n'
                'Все конфеты оппонента достаются сделавшему последний ход. \n')
print(welcome_text)

message = ['твоя очередь', 'да бери уже', 'бери больше', 'не корову проигрываешь',
           'бери быстрее', 'да харош, так долго думать уже']


def player_vs_player():
    candies_total = 2021
    max_take = 28
    count = 0
    player_1 = input('\nВведите свое имя?: ')
    player_2 = input('\nИмя соперника?: ')

    print(f'\Начнем игру!\n')
    print('\nКто ходит первый?\n')

    x = randint(1, 2)
    if x == 1:
        pobed = player_1
        proig = player_2
    else:
        pobed = player_2
        proig = player_1
    print(f' {pobed} ты ходишь первым !')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {pobed} = '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nможно взять только {max_take} конфет {pobed}, попробуй еще: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 1
        else:
            print('Все')

        if count == 1:
            step = int(input(f'\n{choice(message)}, {proig} '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nМожно взять только {max_take} конфет {proig}, попробуй еще: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 0
        else:
            print('кончились конфетки')

    if count == 1:
        print(f'{proig} ПОБЕДИЛ')
    if count == 0:
        print(f'{pobed} ПОБЕДИЛ')


player_vs_player()


def player_vs_bot():
    candies_total = 2021
    max_take = 28
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print('\nкто первый начнет игру.\n')

    pobed = randint(-1, 0)

    print(f'{players[pobed+1]} ты ходишь первым !')

    while candies_total > 0:
        pobed += 1

        if players[pobed % 2] == 'Компьютер':
            print(
                f'\nХодит {players[pobed%2]} \nНа кону {candies_total}. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nходиn,  {players[pobed%2]} \nНа кону {candies_total} {choice(message)}:  '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'На кону осталось {candies_total} \nПобедил {players[pobed%2]}')

player_vs_bot()