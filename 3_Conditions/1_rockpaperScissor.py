# Version 1:

# 1. Player one input: rock | paper | scissors
# 2. Player two input: rock | paper | scissors

# rock vs paper: paper
# scissors vs rock: rock
# scissors vs paper: paper

# Who is the winner? Player 1 or Player 2


player1 = input("Player 1, Enter rock, paper or scissor!: ")
player2 = input("Player 2, Enter rock, paper or scissor!: ")

# print(player1, player2)

if player1 == 'rock' and player2 == 'paper':
    print('Player 2 Wins')
elif player1 == 'rock' and player2 == 'scissor':
    print('Player 1 Wins')
elif player1 == 'rock' and player2 == 'rock':
    print('Its a Tie')
elif player1 == 'paper' and player2 == 'paper':
    print('Its a Tie')
elif player1 == 'paper' and player2 == 'scissor':
    print('Player 2 Wins')
elif player1 == 'paper' and player2 == 'rock':
    print('Player 1 Wins')
elif player1 == 'scissor' and player2 == 'paper':
    print('Player 1 Wins')
elif player1 == 'scissor' and player2 == 'scissor':
    print('Its a Tie')
elif player1 == 'scissor' and player2 == 'rock':
    print('Player 2 Wins')
else:
    print('Invalid Input, Please play again!!')
