from Pr_Solv_Algo_DataStr_UsingPython.ch5_recursion.make_change import (
    change_1,
    change_2,
    change_3,
    change_3_memorize_coins,
    Change,
)


def test_change_1():
    assert change_1([1, 5, 10, 25], 6) == 2
    assert change_1([1, 5, 10, 25], 7) == 3
    assert change_1([1, 5, 10, 25], 0) == 0
    assert change_1([1, 5, 10, 25], 27) == 3
    assert change_1([1, 5, 10, 25], 31) == 3


def test_change_2():
    assert change_2([1, 5, 10, 25], 63) == 6
    assert change_2([1, 5, 10, 25], 6) == 2
    assert change_2([1, 5, 10, 25], 7) == 3
    assert change_2([1, 5, 10, 25], 0) == 0
    assert change_2([1, 5, 10, 25], 27) == 3
    assert change_2([1, 5, 10, 25], 31) == 3
    assert change_2([1, 5, 10, 25], 133) == 9
    assert change_2([1, 5, 10, 25], 99) == 9
    assert change_2([1, 5, 10, 25], 100) == 4

    
def test_change_3():
    assert change_3([1, 5, 10, 25], 63) == 6
    assert change_3([1, 5, 10, 25], 6) == 2
    assert change_3([1, 5, 10, 25], 7) == 3
    assert change_3([1, 5, 10, 25], 0) == 0
    assert change_3([1, 5, 10, 25], 27) == 3
    assert change_3([1, 5, 10, 25], 31) == 3
    assert change_3([1, 5, 10, 25], 133) == 9
    assert change_3([1, 5, 10, 25], 99) == 9
    assert change_3([1, 5, 10, 25], 100) == 4


def test_change_3_memorize_coins():
    assert change_3_memorize_coins([1, 5, 10, 25], 63) == Change(6, [1, 1, 1, 10, 25, 25])
    assert change_3_memorize_coins([1, 5, 10, 25], 6) == Change(2, [1, 5])
    assert change_3_memorize_coins([1, 5, 10, 25], 7) == Change(3, [1, 1, 5])
    assert change_3_memorize_coins([1, 5, 10, 25], 0) == Change(0, [])
    assert change_3_memorize_coins([1, 5, 10, 25], 27) == Change(3, [1, 1, 25])
    assert change_3_memorize_coins([1, 5, 10, 25], 31) == Change(3, [1, 5, 25])
    assert change_3_memorize_coins([1, 5, 10, 25], 133) == Change(9, [1, 1, 1, 5, 25, 25, 25, 25, 25])
    assert change_3_memorize_coins([1, 5, 10, 25], 99) == Change(9, [1, 1, 1, 1, 10, 10, 25, 25, 25])
    assert change_3_memorize_coins([1, 5, 10, 25], 100) == Change(4, [25, 25, 25, 25])
