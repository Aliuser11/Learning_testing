import unittest

class Kalkulator():

    def add(x, y):
        return x+y
        
    def minus(x, y):
        return x-y

    def mnozenie(x,y):
        return x*y
class Test_kalulator(unittest.TestCase):

    def test_dodawanie(add):
        assert Kalkulator.add(2, 4) == 6
    def test_minus(minus):
        assert Kalkulator.minus(5,2) == 3
    

class Test_test_2(unittest.TestCase):
    def test_A(self):
        self.fail("Not implemented")

class Test_math(unittest.TestCase):
    def test_equal(self):
        self.a = 5
        self.b = 5
        self.assertEqual(self.a, self.b)


if __name__ == '__main__':
    unittest.main()


