from Pr_Solv_Algo_DataStr_UsingPython.ch6_sorting_searching.binary_search import binary_s, binary_s_recursion


def test_binary_s():
    assert binary_s([], 6) is False
    assert binary_s([1, 5, 10, 25], 6) is False
    assert binary_s([1], 6) is False
    assert binary_s([1], 1) is True
    assert binary_s([1, 5, 6, 7, 10, 11, 25], 6) is True
    assert binary_s([1, 5, 6, 7, 10, 11, 25], 25) is True
    assert binary_s([1, 5, 6, 7, 10, 11, 25], 1) is True
    assert binary_s([1, 5, 6, 7, 10, 11, 12, 25], 25) is True
    assert binary_s([1, 5, 6, 7, 10, 11, 12, 25], 1) is True
    assert binary_s([1, 5, 6, 7, 10, 11, 12, 25], 7) is True


def test_binary_s_recursion():
    assert binary_s_recursion([], item=6, start=0, end=0-1) is False
    assert binary_s_recursion([1, 5, 10, 25], item=6, start=0, end=4-1) is False
    assert binary_s_recursion([1], item=6, start=0, end=1-1) is False
    assert binary_s_recursion([1], item=1, start=0, end=1-1) is True
    assert binary_s_recursion([1, 5, 6, 7, 10, 11, 25], item=6, start=0, end=7-1) is True
    assert binary_s_recursion([1, 5, 6, 7, 10, 11, 25], item=25, start=0, end=7-1) is True
    assert binary_s_recursion([1, 5, 6, 7, 10, 11, 25], item=1, start=0, end=7-1) is True
    assert binary_s_recursion([1, 5, 6, 7, 10, 11, 12, 25], item=25, start=0, end=8-1) is True
    assert binary_s_recursion([1, 5, 6, 7, 10, 11, 12, 25], item=1, start=0, end=8-1) is True
    assert binary_s_recursion([1, 5, 6, 7, 10, 11, 12, 25], item=7, start=0, end=8-1) is True


