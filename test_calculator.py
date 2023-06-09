import unittest

class Kalkulator():

    def add(x, y):
        return x + y
        
    def minus(x, y):
        return x - y

    def mnozenie(x,y):
        return x * y

    def dzielenie(x, y):
        return x/y

class Test_math(unittest.TestCase):

    def test_equal(self):
        self.a = 5
        self.b = 5
        self.assertEqual(self.a, self.b)
    
    def test_dodawanie(add):
        assert Kalkulator.add(2, 4) == 6
        #assert Kalkulator.add(2, 4) == 5

    def test_minus(minus):
        assert Kalkulator.minus(5, 2) == 3
        #assert Kalkulator.minus(5, 2) == 4

    def test_multi(mnozenie):
        assert Kalkulator.mnozenie(5, 3) == 15
       # assert Kalkulator.mnozenie(5, 3) == 10
    
    def test_dziel(dzielenie):
        assert Kalkulator.dzielenie(5, 5) == 1 
        #assert Kalkulator.dzielenie(5, 5) == 5

if __name__ == '__main__':
    unittest.main()


