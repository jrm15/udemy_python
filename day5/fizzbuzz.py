for i in range(1,101):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)

#FORMA MEJORADA:
for i in range(1,101):
    var=''
    if i%3==0:
        var+='Fizz'
    if i%5==0:
        var+='Buzz'
    if var:#ESTO SIGNIFICA: "SI LA VARIABLE ESTA RELLENA", LO CONTRARIO SERIA "if not var"
        print(var)
    else:
        print (i)