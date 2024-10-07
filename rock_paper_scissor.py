import random

def game():
    choices = ('rock','paper','scissor')
    computer = random.choice(choices)

    user = input('Enter your choices from (rock,paper,scissor):').lower()

    while user not in choices:
        user = input('invalid input,chose again:').lower()
    print(f'The computer choose {computer}, while you choose {user}')

    if user == computer:
        print('The game is a tie')
    if user == 'rock':
        if computer == 'scissor':
            return 'rock smashes scissor, you win'
        else:
            return 'paper covers rock, you lose'
    if user == 'paper':
        if computer == 'rock':
            return 'paper covers rock, you win'
        else:
            return 'scissor cuts paper, you lose'
    if user == 'scissor':
        if computer == 'paper':
            return ' scissor cuts paper, you win'
        else:
            return ' paper covers rock, you lose'
game()
