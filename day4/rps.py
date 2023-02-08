import random

print("ROCK, PAPER, SCISSORS GAME!")

def fun_choose(data: str):
    if(data==0):
        choose="ROCK"
    elif(data==1):
        choose="PAPER"
    else:
        choose="SCISSORS"
    return choose

userdata=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print("You choose: " + fun_choose(userdata))

pcdata=int(random.randrange(0,4))
print("The PC choose: " + fun_choose(pcdata))


if(userdata!=pcdata):
    if(userdata==0):
        if(pcdata==1):
            print("PC WINS!")
        else:
            print("YOU WIN!")
    elif(userdata==1):
        if(pcdata==0):
            print("YOU WIN!")
        else:
            print("PC WINS!")
    elif(userdata==2):
        if(pcdata==0):
            print("PC WINS!")
        else:
            print("YOU WIN!")
else:
    print("DRAW!")