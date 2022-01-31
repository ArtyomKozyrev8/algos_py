from Pr_Solv_Algo_DataStr_UsingPython.ch5_recursion.simple import (
    sum_numbers,
    convert_to_other_system,
    reverse_string,
    check_palindrome,
)


def test_sum_numbers():
    assert sum_numbers([]) == 0
    assert sum_numbers([4]) == 4
    assert sum_numbers([1, 2, 3, 4, 5, 6]) == sum([1, 2, 3, 4, 5, 6])
    assert sum_numbers([1, 2]) == 3


def test_convert_to_other_system():
    assert convert_to_other_system(15, base=16) == 'F'
    assert convert_to_other_system(42, base=2) == '101010'
    assert convert_to_other_system(25, base=2) == '11001'
    assert convert_to_other_system(25, base=16) == '19'
    assert convert_to_other_system(0, base=2) == '0'
    assert convert_to_other_system(1, base=2) == '1'
    assert convert_to_other_system(2, base=2) == '10'
    assert convert_to_other_system(1453, base=16) == '5AD'


def test_reverse_string():
    assert reverse_string("hello") == "hello"[::-1]
    assert reverse_string("") == ""[::-1]
    assert reverse_string("1") == "1"[::-1]
    assert reverse_string("no") == "no"[::-1]


def test_check_palindrome():
    assert check_palindrome("ф") is True
    assert check_palindrome("фф") is True
    assert check_palindrome("фa") is False
    assert check_palindrome("afafa") is True
    assert check_palindrome("abba") is True
