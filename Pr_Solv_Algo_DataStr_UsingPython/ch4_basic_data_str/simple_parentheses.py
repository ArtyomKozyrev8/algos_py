from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.stack import Stack


def check_if_balanced_par(x: str) -> bool:
    """We consider only string which are composed of '(' and ')' """
    if len(x) < 1:
        return False  # if we have less than one parentheses it is clear that not balanced

    if len(x) % 2 != 0:
        return False  # number of parentheses should be even number

    s = Stack()
    for i in x:
        if i == '(':
            s.push(i)
        else:  # if i == ')'
            if s.is_empty():  # prevent error
                return False  # if empty not balanced
            else:
                s.pop()  # remove bracket

    if s.is_empty():
        return True  # if nothing is Stack - balanced

    return False  # otherwise not balanced
