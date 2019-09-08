#Unittest - Serve para crear pruebas dentro del propio codigo

def multiplicar(numero1,numero2):
    return numero1*numero2

resultado = multiplicar(3,5)
#print(resultado)

import unittest

class pruebas(unittest.TestCase):

    def test(self):
        self.assertEqual(multiplicar(3,5),15)
        self.assertEqual(multiplicar(4,4),16)
        self.assertEqual(multiplicar(4,5),20)

if __name__ == '__main__':
    unittest.main()