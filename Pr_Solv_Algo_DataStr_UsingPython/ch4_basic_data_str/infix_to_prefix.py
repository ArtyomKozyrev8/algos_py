from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.stack import Stack
from string import ascii_uppercase, digits


ORDER = dict()
ORDER["("] = 0
ORDER["/"], ORDER["*"] = 1, 1
ORDER["+"], ORDER["-"] = 2, 2

TOKENS = ascii_uppercase + digits


def convert_infix_to_prefix(x: str) -> str:
    """
    Converts from infix to postfix
    :param x: should be composed of ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    and '+', '-', '(', ')', '*', '/'
    :return: postfix string
    """
    postfix = ""  # postfix string
    operators = Stack()  # keep operators here

    for i in x:
        if i in TOKENS:
            postfix += i  # just add them to postfix
        elif i == ")":
            while True:
                temp = operators.pop()
                if temp == "(":
                    break
                postfix += temp
        elif i == "(":
            operators.push(i)
        else:
            while (not operators.is_empty()) and ORDER[operators.peek()] <= ORDER[i]:
                if operators.peek() == '(':
                    break
                postfix += operators.pop()

            operators.push(i)  # add operators after all

    while not operators.is_empty():
        i = operators.pop()
        postfix += i

    return postfix
