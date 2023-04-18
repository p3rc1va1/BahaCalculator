
from unittest import TestCase

from Calculator.calculator import BahaCalculator


class Testing(TestCase):
    #JTL reccomendation divide the test
    
    
    def test_add(self):
        calc = BahaCalculator()
    # test addition
        assert calc.add(3) == 3
        assert calc.add(3) == 6
        
    def test_subs(self):
        calc = BahaCalculator()
    # test subtraction
        assert calc.subtract(3) == -3
        assert calc.subtract(2) == -5
    
        
    def test_mult(self):
        calc = BahaCalculator()
        # test multiplication
        calc.add(2)
        assert calc.multiply(3) == 6
        assert calc.multiply(10) == 60
    
    def test_division(self):
        calc = BahaCalculator()
        # test division
        calc.add(30)
        assert calc.divide(5) == 6
        assert calc.divide(2) == 3

    def test_root(self):
        calc = BahaCalculator()
        # test taking the nth root of a number
        calc.add(36)
        assert calc.root(1) == 36
        assert calc.multiply(12) ==432
        assert calc.root(3) == 7.559526299369238
        
    def test_reset(self):
        calc = BahaCalculator()
        # test resetting the memory
        calc.add(3)
        calc.reset()
        assert calc.memory == 0
    
