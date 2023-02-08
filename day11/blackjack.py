import random

def random_number():
    return int(random.randrange(1,11))

start = str(input('You want to start Blackjack game? Type "y" for start or "n" to cancel game: '))
user_cards = []
user_total = 0
pc_cards = []
pc_total = 0
cont = 'y'


if start == 'y':
    user_cards.append(random_number())
    user_cards.append(random_number())
    user_total = sum(user_cards)
    print(f'Your cards:{user_cards}')
    pc_cards.append(random_number())
    pc_cards.append(random_number())
    pc_total = sum(pc_cards)
    print('Your cards sum:', user_total)
    print(f'Computers first card: {pc_cards[0]}')
    while user_total <= 21 and cont == 'y':
        cont = str(input('Type "y" to get another card, or "n" to pass: '))
        if cont == 'y':
            user_cards.append(random_number())
            user_total = sum(user_cards)
            print(f'Your cards:{user_cards}')
            print('Your cards sum:', user_total)
        else:
            pass
    if user_total<=21:
        while pc_total < 16:
            pc_cards.append(random_number())
            pc_total = sum(pc_cards)
        if pc_total >= user_total and pc_total <= 21:
            print(f'YOU LOOSE,\n\nComputers cards:{pc_cards}\nYour cards:{user_cards}\n\nYour sum cards is: {user_total} and the Computer sum is: {pc_total}')    
        else:
            print(f'YOU WIN,\n\nComputers cards:{pc_cards}\nYour cards:{user_cards}\n\nYour sum cards is: {user_total} and the Computer sum is: {pc_total}')  
    else:
        print(f'You pass 21 and Computers card are: {pc_cards}, YOU LOOSE')
  
else:
    print('The game has end')