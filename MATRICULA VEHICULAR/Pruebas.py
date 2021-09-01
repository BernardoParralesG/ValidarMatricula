import Funciones as Fun
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        resultado = Fun.obtenerLetra('ABC',1)
        self.assertEqual(resultado, 5)

    def test_1(self):
        resultado = Fun.validarMatriculaEspecial('IT')
        self.assertEqual(resultado,5)

    def test_1(self):
        resultado = Fun.validarPrimeraLetra('ABC')
        self.assertEqual(resultado,5)

    def test_1(self):
        resultado = Fun.validarSegundaLetra('AUC')
        self.assertEqual(resultado,3)

    def test_1(self):
        resultado = Fun.validarTerceraLetra('ABC')
        self.assertEqual(resultado,2)

if __name__ == '__main__':
    unittest.main()