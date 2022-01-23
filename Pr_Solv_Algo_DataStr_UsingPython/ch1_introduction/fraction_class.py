from math import gcd


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        assert denominator >= 0, "denominator should be >= 0"
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.numerator}, {self.denominator})"

    def __add__(self, other: "Fraction") -> "Fraction":
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator

        _gcd = gcd(new_num, new_den)
        return Fraction(new_num // _gcd, new_den // _gcd)

    def __sub__(self, other: "Fraction") -> "Fraction":
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator

        _gcd = gcd(new_num, new_den)
        return Fraction(new_num // _gcd, new_den // _gcd)

    def __mul__(self, other: "Fraction") -> "Fraction":
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator

        _gcd = gcd(new_num, new_den)
        return Fraction(new_num // _gcd, new_den // _gcd)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator

        _gcd = gcd(new_num, new_den)
        return Fraction(new_num // _gcd, new_den // _gcd)

    def __eq__(self, other: "Fraction") -> bool:
        first = self.numerator * other.denominator
        second = other.numerator * self.denominator
        return first == second

    def __gt__(self, other: "Fraction") -> bool:
        first = self.numerator * other.denominator
        second = other.numerator * self.denominator
        return first > second
