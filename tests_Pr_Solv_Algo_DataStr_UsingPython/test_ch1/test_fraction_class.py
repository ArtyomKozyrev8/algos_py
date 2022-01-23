from Pr_Solv_Algo_DataStr_UsingPython.ch1_introduction.fraction_class import Fraction

a = Fraction(1, 2)
b = Fraction(2, 3)


def test_str():
    assert str(a) == "1/2"


def test_repr():
    assert repr(a) == f"Fraction(1, 2)"


def test_add():
    assert a + b == Fraction(7, 6)


def test_sub():
    assert a - b == Fraction(-1, 6)


def test_mul():
    assert a * b == Fraction(1, 3)


def test_truediv():
    assert a / b == Fraction(3, 4)


def test_compare():
    assert a < b
