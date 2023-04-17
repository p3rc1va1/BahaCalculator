from calculator import Calculator
def test_calculator():
    # create a new calculator instance
    calc = Calculator()

    # test addition
    assert calc.add(2, 3) == 5
    assert calc.add(-2, 3) == 1
    assert calc.add(0.1, 0.2) == 0.3

    # test subtraction
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(5, -2) == 7
    assert calc.subtract(0.3, 0.2) == 0.1

    # test multiplication
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0.1, 0.2) == 0.02

    # test division
    assert calc.divide(6, 3) == 2
    assert calc.divide(-6, 3) == -2
    assert calc.divide(0.2, 0.1) == 2

    # test taking the nth root of a number
    assert calc.root(4, 81) == 3
    assert calc.root(3, 27) == 3
    assert calc.root(2, 25) == 5

    # test resetting the memory
    calc.add(2, 3)
    calc.reset()
    assert calc.memory == 0
