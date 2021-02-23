#let's play rock paper scissors game
#rock wins scissors / paper wins rock / scissors wins paper 
#update1 : make draw part / make format(make simply)
#update2 : make 'play again' part

import random

player = input('Show your hand(rock, paper, scissors): ')
Type = ['rock', 'paper', 'scissors']
computer = random.choice(Type)
# print(computer)
while True:
    if player == computer:
        print('Draw')
    elif player == 'paper':
        if computer == 'rock':
            print('You win:', 'player {0}, computer {1}'.format(player, computer))
        elif computer == 'scissors':
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
    
    command = input('Want to play again? (y/n): ')
    if command == 'y':
        player = input('Show your hand: ')
    else:
        print('See you')
        break