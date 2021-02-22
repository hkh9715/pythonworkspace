#let's play rock paper scissors game
#rock wins scissors / paper wins rock / scissors wins paper 

import random

player = input('Show your hand: ')
Type = ['rock', 'paper', 'scissors']
computer = random.choice(Type)
# print(computer)
while player == 'paper':
    if computer == 'rock':
        print('You win:', 'player paper,', 'computer rock')
    elif computer == 'scissors':
        print('You lose:', 'player paper,', 'computer scissors')
    else:
        print('Draw')
    break

while player == 'rock':
    if computer == 'scissors':
        print('You win:', 'player rock,', 'computer scissors')
    elif computer == 'paper':
        print('You lose:', 'player rock,', 'computer paper')
    else:
        print('Draw')
    break

while player == 'scissors':
    if computer == 'paper':
        print('You win:', 'player scissors,', 'computer paper')
    elif computer == 'rock':
        print('You lose:', 'player scissors,', 'computer rock')
    else:
        print('Draw')
    break