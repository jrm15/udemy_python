import math

coverage = 5
height = int(input("Tell me the height: "))
weight = int(input("Tell me the weight: "))

def calc_cans(h, w):
    cans = math.ceil((h*w)/coverage)
    #REDONDEA HACIA ARRIBA
    return cans

cans = calc_cans(height, weight)
print(f'You need {cans} cans of paint')
