#let's play rock paper scissors game
#rock wins scissors / paper wins rock / scissors wins paper 
#update1 : make draw part / make format(make simply)
#update2 : make 'play again' part
#update3 : UpperLower / random
#update4 : enter when new game starts
#update5 : make error message by 'try&except' / make sure to restart the game by 'continue' / make odds

import random

Type = ['rock', 'paper', 'scissors']
def error1(e1):
    if e1 not in Type:
        raise ValueError
# def error2(e2):
#     if e2 != 'y':
#         raise ValueError
num_win = 0
num_draw = 0
num_lose = 0

while True:
    a = input('\nShow your hand(rock, paper, scissors): ')
    player = a.lower()
    try:
        error1(player)
    except ValueError:
        print('PLEASE type one of these(rock, paper, scissors)')
        continue
    computer = random.choice(Type)
    # print(computer)

    if player == computer:
        print('Draw')
        num_draw += 1
    elif player == 'paper':
        if computer == 'rock':
            print('You win:', 'player {0}, computer {1}'.format(player, computer))
            num_win += 1
        else:
            print('You lose:', 'player {0}, computer {1}'.format(player, computer))
            num_lose += 1

    elif player == 'rock':
        if computer == 'scissors':
            print('You win:', 'player {0}, computer {1}'.format(player, computer))
            num_win += 1
        else:
            print('You lose:', 'player {0}, computer {1}'.format(player, computer))
            num_lose += 1

    elif player == 'scissors':
        if computer == 'paper':
            print('You win:', 'player {0}, computer {1}'.format(player, computer))
            num_win += 1
        else:
            print('You lose:', 'player {0}, computer {1}'.format(player, computer))
            num_lose += 1

    b = input('Your odds(win:draw:lose): {0}:{1}:{2} \nWant to play again? Press ENTER: '.format(num_win, num_draw, num_lose))
    # print(b)
    if b != "":
        print('\nSee you')
        break
    else:
        print('play again')