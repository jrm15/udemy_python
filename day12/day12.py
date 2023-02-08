""""
ERROR:

enemies = 1

def increase_enemies():
    enemies += 1
    print(f'Enemies in function: {enemies}')

increase_enemies()
print(f'Enemies out function: {enemies}')
"""

enemies = 1

def increase_enemies():
    global enemies 
    enemies += 1
    print(f'Enemies in function: {enemies}')

increase_enemies()
print(f'Enemies out function: {enemies}')

"""
LAS CONSTANTES GLOBALES SE DEFINEN EN MAYUSCULAS Y SON LAS QUE NUNCA SE VAN A MODIFICAR:

PI = 3.14159
URL = "https://www.google.com"
"""