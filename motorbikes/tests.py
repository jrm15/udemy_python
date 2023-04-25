from unittest import TestCase
from unittest.mock import patch
from motorbikes.moto_class import Moto


class TestMoto(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.moto_ex = {
        "color": "negro",
        "matricula": "0000MSN",
        "combustible": 20,
        "ruedas": 2,
        "marca": "Yamaha",
        "modelo": "XMAX",
        "fabricacion": 2023,
        "velocidad_punta": 200,
        "peso": 500,
        "arranque_motor": False
        }

    @patch("motorbikes.moto_class.Moto.metodo_arrancar")
    def test_arrancar(self, mock_sesion):
        Moto()