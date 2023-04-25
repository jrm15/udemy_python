from unittest import TestCase
from unittest.mock import patch

from motorbikes.moto_class import Moto


class TestMoto(TestCase):

    moto_ex = Moto(color="negro", matricula="0000MSN", combustible=10, ruedas=2, marca="Yamaha", modelo="XMAX",
                   fabricacion=2023, velocidad_punta=200, peso=500, arranque_motor=False)

    def test_crear_moto(self):
        moto_try = Moto(color="negro", matricula="0000MSN", combustible=30, ruedas=2, marca="Yamaha", modelo="XMAX",
                        fabricacion=2023, velocidad_punta=200, peso=500, arranque_motor=False)
        self.assertEqual(moto_try.color, "negro")
        self.assertEqual(moto_try.matricula, "0000MSN")
        # asi con todos

    def test_error_crear_moto_color(self):
        with self.assertRaises(ValueError):
            Moto(color=1, matricula="0000MSN", combustible=30, ruedas=2, marca="Yamaha", modelo="XMAX",
                 fabricacion=2023, velocidad_punta=200, peso=500, arranque_motor=False)

    def test_metodo_arrancar(self):
        result = self.moto_ex.metodo_arrancar()
        expected = "El motor ha arrancado"

        self.assertEqual(result, expected)

    def test_metodo_detener(self):
        result = self.moto_ex.metodo_detener()
        expected = "El motor ya estaba detenido"

        self.assertEqual(result, expected)

    def test_metodo_respostar(self):
        result = self.moto_ex.metodo_repostar()
        expected = "Puedes respostar 10 litros hasta el limite"

        self.assertEqual(result, expected)

