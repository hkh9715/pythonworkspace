#let's play rock paper scissors game
#rock wins scissors / paper wins rock / scissors wins paper 
#update1 : make draw part / make format(make simply)
#update2 : make 'play again' part
#update3 : UpperLower / random
#update4 : enter when new game starts


while True:
    import random
    try:
        a = input('\nShow your hand(rock, paper, scissors): ')
        player = a.lower()
        Type = ['rock', 'paper', 'scissors']
        computer = random.choice(Type)
        # print(computer)
    
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
    except:
        print('please type one of these(rock, paper, scissors)')

    b = input('Want to play again? (y/n): ')
    command = b.lower()
    if command != 'y':
        print('\nSee you')
        break