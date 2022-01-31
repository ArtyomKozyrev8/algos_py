from typing import List, Union


def sum_numbers(x: List[Union[int, float]]) -> Union[int, float]:
    if len(x) == 0:
        return 0

    if len(x) == 1:
        return x[0]

    return x[0] + sum_numbers(x[1:])


def convert_to_other_system(x: int, base=2):
    assert x >= 0, "x should be >= 0"
    assert base in (2, 8, 16), "base should be 2, 8 or 16"

    basis = "0123456789ABCDEF"

    if x < base:
        return basis[x]

    temp = x // base

    return convert_to_other_system(temp, base=base) + basis[x - base * temp]


def reverse_string(x: int):
    if len(x) <= 1:
        return x

    return reverse_string(x[1:]) + x[0]


def check_palindrome(x: str):
    if len(x) <= 1:
        return True

    if x[0] != x[-1]:
        return False

    return check_palindrome(x[1: len(x)-1])
