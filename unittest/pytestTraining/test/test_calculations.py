import pytest

from src.calculations import Calculations


    class TestCalculations:
        calc = Calculations()



    def test_add(self):
        res = calc.add(n1= 10 , n2= 5)
        assert res == 15, 'Addition error '

    def test_sub(self):
        res = calc.sub(n1= 10, n2= 5)
        assert res == 15, 'Subtraction error '

    def test_mul(self):
        res = calc.mul(n1= 10, n2= 5)
        assert res == 50, 'Multiplication error '


    def test_div(self):
        res = calc.div(n1= 10, n2= 5)
        assert res == 2.0, 'Division error '
