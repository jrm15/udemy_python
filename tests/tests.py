import unittest
from main import suma, operation
from unittest.mock import patch, Mock


class TestOp(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(), 2)

    @patch("main.suma")
    def test_operation(self, mock_suma):
        mock_suma.return_value = 3
        self.assertEqual(operation(), True)


if __name__ == '__main__':
    unittest.main()
