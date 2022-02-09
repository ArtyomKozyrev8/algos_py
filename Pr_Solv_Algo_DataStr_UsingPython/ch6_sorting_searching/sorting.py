from typing import List, Any


def bubble_sort(x: List[Any]) -> List[Any]:
    for i in range(len(x)):
        swapped = False
        for j in range(len(x) - i - 1):
            if x[j] >= x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                swapped = True

        if swapped is False:
            return x

    return x


def selection_sort(x: List[Any]) -> List[Any]:
    for i in range(len(x)):
        max_i = 0
        for j in range(len(x) - i):
            if x[j] >= x[max_i]:
                max_i = j

        x[max_i], x[len(x) - i - 1] = x[len(x) - i - 1], x[max_i]

    return x
