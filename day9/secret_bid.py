from replit import clear

bids = {}

argument = 'yes'

print('Welcome to the secret auction program.')


while argument == 'yes':
    name = str(input('What is your name?: '))
    bid = int(input('What is your bid?: $'))
    bids[name] = bid
    argument = str(input('Are there any other bidders? Type "yes" or "no".'))
    clear()


max_name = ''
max_bid = 0
for key in bids:
    if int(bids[key])>max_bid:
        max_bid = bids[key]
        max_name = key
    else:
        pass


print(f'The winner is {max_name} with a bid of ${max_bid}')