class User:
    pass

user_1 = User()
user_1.id = '001'
user_1.name = 'Javi'
user_1.age = 25
print(user_1.name)

user_2 = User()
user_2.id = '002'
user_2.name = 'Marta'
user_2.age = 26
print(user_2.name)

# si los objetos van a ser iguales, se utilizan los constructores (initialize)


class Alumn:
    def __init__(self, name, curse):
        self.name = name
        self.curse = curse
        self.school = 'Carmelo'

# SIEMPRE SE AÑADE EL PARAMETRO SELF EL PRIMERO
    def up_curse(self):
        self.curse += 1


alumn_1 = Alumn('Javi', 2)
print(alumn_1.name)
print(alumn_1.school)
alumn_1.up_curse()
print(alumn_1.curse)