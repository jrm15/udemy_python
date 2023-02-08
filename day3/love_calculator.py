print("WELCOME TO THE LOVE COMPABILITY CALCULATOR")

name1=str(input("Write first of the names: "))
name2=str(input("Write second name: "))


def passfunc(item, obj):
    comp=0
    for e in obj:
        for i in item:
            if i!= e:
                continue
            comp+=1
    return comp

    
truenum=passfunc(name1, "TRUE")+passfunc(name2, "TRUE")
lovenum=passfunc(name1, "LOVE")+passfunc(name2, "LOVE")

solution=str(truenum) + str(lovenum)

print(f"Your percentaje of compability is {solution}%")