#DICCIONARIES:

my_diccionary = {
    'Hola': 'Un saludo',
    'Adios': 'Una despedida'
}
print(my_diccionary['Hola'])


#AÑADIR ELEMENTO:

my_diccionary['Hello'] = 'Un saludo en ingles'


#BORRAR DICCIONARIO:

my_diccionary = {}


#EDITAR UN ELEMENTO:

my_diccionary['Hola'] = 'Un saludo en español'


#BUCLES EN DICCIONARIOS:

for key in my_diccionary:
    print(key)
    print(my_diccionary[key])


#ANIDACION DE LISTAS Y DICCIONARIOS EN DICCIONARIOS:

travel = {
    "France" : {'cities_visited' : ['París', 'Hamburg', 'Dijon'], 'cities_not_visited' : ['Marseille'], 'total_visits' : 4},
    "Germany" : ['Berlin', 'Hamburg']
}
travel_list = [
    {
    'country' : 'France',
    'cities_visited' : ['París', 'Lille', 'Dijon'],
    'cities_not_visited' : ['Marseille'],
    'total_visits' : 4
    },
    {
    'country' : 'Berlin',
    'cities_visited' : ['Berlin', 'Hamburg'],
    'cities_not_visited' : ['Stuttgart'],
    'total_visits' : 2
    },
]