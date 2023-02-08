import random

print("Welcome to Less or High Game!\nI'm thinking on a number between 1 and 100.")

number = int(random.randrange(1,101))
print(number)
user_number = 0
lifes = 0
diff = str(input('Choose a difficulty. Type "easy" or "hard": '))

def compare(num: int, lif: int):
    if num < number:
        lif -= 1
        print('Too low')
    elif num > number:
        lif -= 1
        print('Too high')
    else:
        lif = 100
        print('YOU WIN')
    return  lif


if diff == 'hard':
    lifes = 5
else:
    lifes = 10

while lifes > 0 and lifes != 100:
    print(f'You have {lifes} attemps remainig to guess the number.')
    user_number = int(input('Make a guess: '))
    lifes = compare(user_number, lifes)

if lifes == 0:
    print('YOU LOOSE')