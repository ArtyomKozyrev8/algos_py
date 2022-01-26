from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.stack import Stack


def convert_from_decimal(x: int, base: int) -> str:
    """
    can convert x () to bin, oct, hex forms
    :param x: positive or zero integer
    :param base: can be 2, 8, 16
    :return: string which represents another form of digit
    """
    assert x >= 0, "x should be >= 0"
    assert base in (2, 8, 16), "base should be 2, 8 or 16"

    if x == 0:
        return "0"

    basis = "0123456789ABCDEF"

    s = Stack()
    while x >= base:
        temp = x // base
        s.push(basis[x - base * temp])
        x = temp

    if x != 0:
        s.push(basis[x])

    res = ""
    while not s.is_empty():
        res += s.pop()

    return res
