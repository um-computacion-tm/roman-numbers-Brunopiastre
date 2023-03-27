import unittest
def decimal_to_Roman(decimal):

    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV","I"]

numeral= " "
i=0

while entero > 0
    
class test_decimal(unittest.TestCase):

    def test_1 (self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado,"I")

    def test_2(self):
        resultado=decimal_to_roman () 

    def test_4(self):
        resultado=decimal_to_roman(4)
        self.assertEqual(resultado,"IV")

    def test_5(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, "V")

    def test_9(self):
        resultado=decimal_to_roman(9)
        self.assertEqual(resultado,"IX")

    def test_10(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, "X")
    
    
if __name__ == "__main__":
    unittest.main()

