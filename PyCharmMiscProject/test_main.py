import unittest
from main import Rectangulo, Circulo, CalculadoraArea, es_primo

class TestLaboratorio(unittest.TestCase):

    def test_area_rectangulo(self):
        rectangulo = Rectangulo(4, 5)
        calculadora = CalculadoraArea()
        self.assertEqual(calculadora.calcular(rectangulo), 20)

    def test_es_primo(self):
        self.assertTrue(es_primo(7))
        self.assertFalse(es_primo(4))

if __name__ == "__main__":
    unittest.main()