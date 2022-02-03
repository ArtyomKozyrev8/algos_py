from typing import List
from collections import namedtuple


def change_1(coins_list: List[int], value: int) -> int:
    """
    Answers the smallest number of coins we need to exchange value.
    Actually very slow without memoization.
    Do not use for numbers value more than 30 and coins_list Len > 4
    """
    if value in coins_list:
        return 1

    if value == 0:
        return 0  # this is exit from recursion

    min_num_coins = value

    for i in coins_list:
        if i <= value:
            cur_num_coins = 1 + change_1(coins_list, value - i)
            if cur_num_coins < min_num_coins:
                min_num_coins = cur_num_coins

    return min_num_coins    # we get it only after all recursion stuff is finished


def change_2(coins_list: List[int], value: int) -> int:
    """Answers the smallest number of coins we need to exchange value. Version with memoization"""
    memory = dict()

    def inner(_coins_list: List[int], _value: int) -> int:
        if _value in _coins_list:
            return 1  # this is exit from recursion

        if _value == 0:
            return 0  # this is exit from recursion

        min_num_coins = _value

        for i in _coins_list:
            if i <= _value:
                if _value - i in memory.keys():
                    cur_num_coins = 1 + memory[_value - i]
                else:
                    memory[_value - i] = inner(_coins_list, _value - i)
                    cur_num_coins = 1 + memory[_value - i]

                if cur_num_coins < min_num_coins:
                    min_num_coins = cur_num_coins

        return min_num_coins    # we get it only after all recursion stuff is finished

    return inner(coins_list, value)


def change_3(coins_list: List[int], value: int) -> int:
    """Dynamic programming solution"""
    memory = dict()
    memory[0] = 0  # this is basis value, we need 0 coins to exchange 0 amount of money
    for i in range(value + 1):  # start building our table step by step
        m = i
        for v in coins_list:  # check all possible coins to find smallest
            if i - v >= 0:
                if m >= 1 + memory[i - v]:
                    m = 1 + memory[i - v]
        memory[i] = m

    return memory[value]


Change = namedtuple("Change", ["num_coins", "coins"])


def change_3_memorize_coins(coins_list: List[int], value: int) -> Change:
    """Dynamic programming solution. Which remembers what coins were used"""
    memory = dict()
    memory[0] = Change(0, list())  # this is basis value, we need 0 coins to exchange 0 amount of money
    for i in range(value + 1):  # start building our table step by step
        m = i
        used_coins = []
        for v in coins_list:  # check all possible coins to find smallest
            if i - v >= 0:
                if m >= 1 + memory[i - v].num_coins:
                    m = 1 + memory[i - v].num_coins
                    used_coins = memory[i - v].coins + [v]
        memory[i] = Change(m, sorted(used_coins))

    return memory[value]
