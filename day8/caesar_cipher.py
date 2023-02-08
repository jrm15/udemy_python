from alphabet import alphabet


def caesar(word, number, act):
    print('Your new phrase is: ', end='')
    for lett in word:
        if lett in alphabet:#IMPORTANTE PARA BUSCAR CARACTER EN LISTAS
            ind = alphabet.index(lett)
            if act==1:
                ind += number
            else:
                ind -= number
            print(alphabet[ind], end='')
        else:
            print(lett, end='')


cont = 1
while cont==1:
    action = int(input('What u want to do?\nIf you want to Codify, press 1\nIf you want to Decodify press 2\n'))
    word = input('Tell me the phrase: ')
    number = int(input('Tell me the shift number: '))
    caesar(word, number, action)
    cont = int(input('\nWant to continue? Press 1 for yes or 2 for no: '))