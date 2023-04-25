from motorbikes.moto_class import Moto


moto1 = Moto(color="negro", matricula="0000MSN", combustible=30, ruedas=2, marca="Yamaha", modelo="XMAX",
             fabricacion=2023, velocidad_punta=200, peso=500, arranque_motor=False)

moto2 = Moto(color="blanco", matricula="0000MSN", combustible=30, ruedas=2, marca="Yamaha", modelo="XMAX",
             fabricacion=2023, velocidad_punta=200, peso=500, arranque_motor=False)


print(moto1)

print(moto1.get_marca())

moto1.motor()

print(moto1)
