
import unittest
class pr�bka():

    def add(x, y):
        return x+y
        
    def minus(x, y):
        return x-y

    def mnozenie(x,y):
        return x*y

class Test_probka(unittest.TestCase):
    def test_add(add):
        assert pr�bka.add(3, 4) == 7

if __name__ == '__main__':
    unittest.main()

