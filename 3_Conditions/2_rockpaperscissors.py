# Version 2:

# 1. Player one input: rock | paper | scissors
# 2. Player two input: rock | paper | scissors

# rock vs paper: paper
# scissors vs rock: rock
# scissors vs paper: paper

# Who is the winner? Player 1 or Player 2


player1 = input("Player 1, Enter rock, paper or scissors!: ")
player2 = input("Player 2, Enter rock, paper or scissors!: ")

player1 = player1.lower()
player2 = player2.lower()

if ((player1 == 'scissors' or player1 == 'paper' or player1 == 'rock') and (player2 == 'scissors' or player2 == 'paper' or player2 == 'rock')):
    if (player1 == player2):
        print('Its a Tie!!')

    elif player1 == 'rock':
        if player2 == 'scissors':
            print('Player 1 Wins')
        if player2 == 'paper':
            print('Player 2 wins')

    elif player1 == 'paper':
        if player2 == 'scissors':
            print('Player 1 Wins')
        if player2 == 'rock':
            print('Player 2 wins')

    elif player1 == 'scissors':
        if player2 == 'paper':
            print('Player 1 Wins')
        if player2 == 'rock':
            print('Player 2 wins')
    else:
        print('Invalid Input!!!')
else:
    print('Invalid Input!!!')
