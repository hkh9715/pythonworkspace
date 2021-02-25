#let's play rock paper scissors game
#rock wins scissors / paper wins rock / scissors wins paper 
#update1 : make draw part / make format(make simply)
#update2 : make 'play again' part
#update3 : UpperLower / random
#update4 : enter when new game starts
#update5 : make error message by 'try&except' / make sure to restart the game by 'continue' / make odds
#update6 : make odds detail / make definitions for simple code / make color for situation

import random

Type = ['rock', 'paper', 'scissors']
def error1(e1):
    if e1 not in Type:
        raise ValueError
def result_win(player, computer):
    print('\033[44m'+'You win:', 'player {0}, computer {1}'.format(player, computer)+'\033[0m')
def result_lose(player, computer):
    print('\033[41m'+'You lose:', 'player {0}, computer {1}'.format(player, computer)+'\033[0m')

# def error2(e2):
#     if e2 != 'y':
#         raise ValueError
num_win = 0
num_draw = 0
num_lose = 0
num_game = 1
odds = 0.0

while True:
    a = input('\nGame{0}\nShow your hand(rock, paper, scissors): '.format(num_game))
    player = a.lower()
    try:
        error1(player)
    except ValueError:
        print('PLEASE type one of these(rock, paper, scissors)')
        continue

    num_game += 1
    computer = random.choice(Type)
    # print(computer)

    if player == computer:
        print('Draw')
        num_draw += 1
    elif player == 'paper':
        if computer == 'rock':
            result_win(player, computer)
            num_win += 1
        else:
            result_lose(player, computer)
            num_lose += 1

    elif player == 'rock':
        if computer == 'scissors':
            result_win(player, computer)
            num_win += 1
        else:
            result_lose(player, computer)
            num_lose += 1

    elif player == 'scissors':
        if computer == 'paper':
            result_win(player, computer)
            num_win += 1
        else:
            result_lose(player, computer)
            num_lose += 1

    try:
        odds = num_win / (num_game-num_draw) * 100
        b = input('Your odds(win:draw:lose, odds): {0}:{1}:{2}, {3}% \nWant to play again? Press ENTER: '.format(num_win, num_draw, num_lose, odds))
    except:
        b = input('Your odds(win:draw:lose, odds): {0}:{1}:{2}, {3}% \nWant to play again? Press ENTER: '.format(num_win, num_draw, num_lose, odds))

    if b != "":
        print('\nSee you')
        break
    else:
        print('play again')