from typing import List, Any


def binary_s(x: List[Any], item: Any) -> bool:
    """
    Answers if item is in x
    :param x: x is sorted List
    :param item: we search for the item in the list
    :return: True / False
    """
    if len(x) == 0:
        return False

    start = 0
    end = len(x) - 1
    center = (end + start) // 2

    while start <= center <= end:
        if item == x[center]:
            return True
        elif item > x[center]:
            start = center + 1
        else:
            end = center - 1
        center = (end + start) // 2

    return False


def binary_s_recursion(x: List[Any], item: Any, start: int, end: int) -> bool:
    if len(x) == 0:
        return False

    center = (end + start) // 2

    if not (start <= center <= end):
        return False

    if item == x[center]:
        return True
    elif item > x[center]:
        start = center + 1
    else:
        end = center - 1

    return binary_s_recursion(x, item, start, end)
