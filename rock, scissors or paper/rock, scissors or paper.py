import random

while True:
    choices = ['paper', 'rock', 'scissors']

    computer = random.choice(choices)
    player = True

    while player not in choices:
        player = input('rock, paper or scissors?: ').lower()

    if computer == player:
        print(f"computer: {computer}")
        print(f"player: {player}")
        print('Tie')

    elif computer == 'rock':
        if player == 'scissors':
            print(f"computer: {computer}")
            print(f"player: {player}")
            print('You lose')
        elif player == 'paper':
            print(f"computer: {computer}")
            print(f"player: {player}")
            print('You win')

    elif computer == 'paper':
        if player == 'scissors':
            print(f"computer: {computer}")
            print(f"player: {player}")
            print('You win')
        elif player == 'rock':
            print(f"computer: {computer}")
            print(f"player: {player}")
            print('You lose')

    elif computer == 'scissors':
        if player == 'rock':
            print(f"computer: {computer}")
            print(f"player: {player}")
            print('You win')
        elif player == 'paper':
            print(f"computer: {computer}")
            print(f"player: {player}")
            print('You lose')

    command = input('Do you want play again? ')
    if command != 'yes':
        break

print('Bye!')
