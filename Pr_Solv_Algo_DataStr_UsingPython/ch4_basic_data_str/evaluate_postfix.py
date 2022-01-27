from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.stack import Stack
from operator import add, sub, truediv, mul

OPERATORS = {
    "*": mul,
    "/": truediv,
    "+": add,
    "-": sub,
}


def evaluate_postfix(x: str) -> float:
    """
    Calculates results of postfix expression.
    :param x: should be postfix expression operators and tokens should be separate by ' '
    Expression should be composed of positive int or float numbers and operators '*', '/', '+', '-'
    :return: result of postfix expression evaluation
    """
    s = Stack()
    x = x.split(' ')

    if len(x) == 1:
        return float(x[0])

    for i in x:
        if i not in ('*', '/', '+', '-'):
            s.push(float(i))
        else:
            a = s.pop()
            b = s.pop()
            s.push(OPERATORS[i](b, a))

    return s.pop()
