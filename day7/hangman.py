from words import words_list
import random

print('WELCOME TO THE HANGMAN:\n\n(YOU START WITH 6 LIVES)\n\nTHE WORD IS:\n')

random_number=int(random.randrange(1,40))
word=words_list[random_number]
word_def=''

vidas = 6


word_def = '_'*len(word)

print(word_def)

while vidas!=0 and word!=word_def:
    letra=str(input("\nCHOOSE A LETTER: "))
    var=0
    t=0
    for i in word:
        if word_def[t] == '_':
            if i==letra:
                var+=1
                word_def=word_def[:t]+i+word_def[t+1:]
            else:
                word_def=word_def[:t]+'_'+word_def[t+1:]
        t+=1
    if var==0:
        vidas-=1
    print('\n', word_def)
    print('\n LIVES: ', vidas)

if(vidas==0):
    print('\nYOU LOOSE :(\nTHE WORD WAS:', word)
if(word==word_def):
    print('\nYOU WIN :D')