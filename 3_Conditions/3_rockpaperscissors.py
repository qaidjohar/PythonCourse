# Version 2: rock Paper Scissors with Computer

# Play against the computer

# Enter Input: rock | paper | scissors
# Take Computer Input: randint

# rock vs paper: paper
# scissors vs rock: rock
# scissors vs paper: paper

import random

player = input("Player , Enter rock, paper or scissors!: ")

player = player.lower()

randomval = random.randint(0, 2)
if randomval == 0:
    computer = 'rock'
elif randomval == 1:
    computer = 'paper'
else:
    computer = 'scissors'

print(f'Computer has selected: {computer}')


if ((player == 'scissors' or player == 'paper' or player == 'rock')):
    if (player == computer):
        print('Its a Tie!!')

    elif player == 'rock':
        if computer == 'scissors':
            print('Player Wins!!')
        if computer == 'paper':
            print('Computer Wins')

    elif player == 'paper':
        if computer == 'scissors':
            print('Player Wins!!')
        if computer == 'rock':
            print('Computer Wins')

    elif player == 'scissors':
        if computer == 'paper':
            print('Player Wins!!')
        if computer == 'rock':
            print('Computer Wins')
    else:
        print('Invalid Input!!!')
else:
    print('Invalid Input!!!')
