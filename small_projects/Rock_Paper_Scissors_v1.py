#let's play rock paper scissors game
#rock wins scissors / paper wins rock / scissors wins paper 
#update1 : make draw part / make format(make simply)
#update2 : make 'play again' part
#update3 : UpperLower / random
#update4 : enter when new game starts
#update5 : make error message by 'try&except'

import random

Type = ['rock', 'paper', 'scissors']
def error1(e1):
    if e1 not in Type:
        raise ValueError
# def error2(e2):
#     if e2 != 'y':
#         raise ValueError

while True:
    a = input('\nShow your hand(rock, paper, scissors): ')
    player = a.lower()
    try:
        error1(player)
    except ValueError:
        print('please type one of these(rock, paper, scissors)')
    computer = random.choice(Type)
    # print(computer)

    if player == computer:
        print('Draw')
    elif player == 'paper':
        if computer == 'rock':
            print('You win:', 'player {0}, computer {1}'.format(player, computer))
        else:
            print('You lose:', 'player {0}, computer {1}'.format(player, computer))

    elif player == 'rock':
        if computer == 'scissors':
            print('You win:', 'player {0}, computer {1}'.format(player, computer))
        else:
            print('You lose:', 'player {0}, computer {1}'.format(player, computer))

    elif player == 'scissors':
        if computer == 'paper':
            print('You win:', 'player {0}, computer {1}'.format(player, computer))
        else:
            print('You lose:', 'player {0}, computer {1}'.format(player, computer))

    # num_win = 
    # b = input('Want to play again? (y/n): \nYour odds: {0}:{1}:{2}'.format(num_win, num_draw, num_lose))
    b = input('Want to play again? Press ENTER: ')
    # print(b)
    if b is not None:
        print('\nSee you')
        break
    # try:
    #     error2(command)
    # except ValueError:
    #     print('If you want to, type y!')
    # if command != 'y':
    #     print('\nSee you')
    #     break