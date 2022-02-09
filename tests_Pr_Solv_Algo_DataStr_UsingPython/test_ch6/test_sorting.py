from Pr_Solv_Algo_DataStr_UsingPython.ch6_sorting_searching.sorting import (
    bubble_sort,
    selection_sort,
)


def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert bubble_sort([1, 4, 5, 2, 7, 0]) == sorted([1, 4, 5, 2, 7, 0])
    assert bubble_sort([0, 9, 9, 8, 7, 5, 3]) == sorted([0, 9, 9, 8, 7, 5, 3])
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == sorted([54, 26, 93, 17, 77, 31, 44, 55, 20])


def test_selection_sort():
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([1, 2, 3]) == [1, 2, 3]
    assert selection_sort([1, 4, 5, 2, 7, 0]) == sorted([1, 4, 5, 2, 7, 0])
    assert selection_sort([0, 9, 9, 8, 7, 5, 3]) == sorted([0, 9, 9, 8, 7, 5, 3])
    assert selection_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert selection_sort([3, 2, 1]) == [1, 2, 3]
    assert selection_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == sorted([54, 26, 93, 17, 77, 31, 44, 55, 20])
