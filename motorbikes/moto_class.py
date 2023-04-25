import random


class Moto:

    max_litres = 20

    def __init__(self, color: str, matricula: str, combustible: int, ruedas: int, marca: str, modelo: str,
                 fabricacion: int, velocidad_punta: int, peso: int, arranque_motor: bool = False):
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError("Color tiene que ser de tipo string")
        if isinstance(matricula, str):
            self.matricula = matricula
        else:
            raise ValueError("Matricula tiene que ser de tipo entero")
        if combustible <= self.max_litres:
            self.combustible = combustible
        else:
            self.combustible = self.max_litres
        self.ruedas = ruedas
        self.__marca = marca
        self.modelo = modelo
        self.fabricacion = fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.arranque_motor = arranque_motor

    def __eq__(self, other):
        return self.velocidad_punta == other.velocidad_punta

    def __lt__(self, other):
        return self.velocidad_punta < other.velocidad_punta

    def __gt__(self, other):
        return self.velocidad_punta > other.velocidad_punta

    def __str__(self):
        return f"color = {self.color}\n" \
               f"matricula = {self.matricula}\n" \
               f"combustible = {self.combustible}\n" \
               f"ruedas = {self.ruedas}\n" \
               f"marca = {self.__marca}\n" \
               f"modelo = {self.modelo}\n" \
               f"fabricacion = {self.fabricacion}\n" \
               f"velocidad punta = {self.velocidad_punta}\n" \
               f"peso = {self.peso}\n" \
               f"arranque motor = {self.arranque_motor}"

    def __add__(self, other):
        lista = [self.color, other.color]
        color_random = random.choice(lista)
        if self.fabricacion == other.fabricacion and self.ruedas == other.ruedas and self.__marca == other.__marca:
            return Moto(color=color_random, matricula="", combustible=self.combustible + other.combustible,
                        ruedas=0, marca="", modelo="", fabricacion=0, velocidad_punta=self.velocidad_punta
                        + other.velocidad_punta, peso=self.peso + other.peso)

    def get_marca(self):
        return self.__marca

    def motor(self):
        if not self.arranque_motor:
            self.arranque_motor = True
        else:
            self.arranque_motor = False

    def metodo_arrancar(self):
        if self.arranque_motor:
            msg = "El motor ya estaba en marcha"
        else:
            msg = "El motor ha arrancado"
        return msg

    def metodo_detener(self):
        if self.arranque_motor:
            msg = "El motor se ha detenido"
        else:
            msg = "El motor ya estaba detenido"
        return msg

    def metodo_repostar(self):
        if self.combustible < self.max_litres:
            rest = self.max_litres - self.combustible
            msg = f"Puedes respostar {rest} litros hasta el limite"
        else:
            msg = "El deposito de combustible esta lleno"
        return msg


