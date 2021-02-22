#let's play rock paper scissors game
#rock wins scissors / paper wins rock / scissors wins paper 
#update : make draw part / make format(make simply)
import random

player = input('Show your hand: ')
Type = ['rock', 'paper', 'scissors']
computer = random.choice(Type)
# print(computer)
while True:
    if player == computer:
        print('Draw')
    elif player == 'paper':
        if computer == 'rock':
            print('You win:', 'player {0}, computer {1}'.format(player, computer))
        if computer == 'scissors':
            print('You lose:', 'player {0}, computer {1}'.format(player, computer))

    elif player == 'rock':
        if computer == 'scissors':
            print('You win:', 'player {0}, computer {1}'.format(player, computer))
        if computer == 'paper':
            print('You lose:', 'player {0}, computer {1}'.format(player, computer))

    elif player == 'scissors':
        if computer == 'paper':
            print('You win:', 'player {0}, computer {1}'.format(player, computer))
        if computer == 'rock':
            print('You lose:', 'player {0}, computer {1}'.format(player, computer))
    
    break