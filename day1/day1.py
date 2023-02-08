print("Hello " + input("What's your name?"))
#EJECUTA EL INPUT ANTES SI ESTA DENTRO DE UN PRINT



print("Hello\nWhat's your name?")

a = input()
print("Your name has " + str(len(a)) + " characters")
#TIENES QUE PASAR A STRING EL ENTERO PARA IMPRIMIRLO ASI

print("Characters of your name: ", len(a))
#O SIN PASARLO A STRING SE HARIA ASI



#MANERA EFECTIVA DE ALMACENAR UNA VARIABLE CON UN PRINT:
#print("a = ")
#a=input()

a = input("a = ")
b = input("b = ")
print("a = ", b)
print("b = ", a)




#EJERCICIO FINAL

print("Welcome to the Band Name Generator")

city = input("What's the name of the city you grew up? \n")
pet = input("What's your pet name? \n")
print("Your band name could be", city, pet)

#SI INCLUIMOS \n AL FINAL DEL INPUT, GENERA LA LINEA DE ESCRITURA EN LA LINEA DE ABAJO DEL PRINT