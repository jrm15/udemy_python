from prettytable import PrettyTable

my_tabble = PrettyTable()
my_tabble.align = "c"

my_tabble.add_column('Pokemon', ['Pikachu', 'Bulbasaur', 'Charmander', 'Squirtle'])
my_tabble.add_column('Type', ['Electric', 'Plant', 'Fire', 'Watter'])
print(my_tabble)
