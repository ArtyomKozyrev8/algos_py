from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.stack import Stack

MATCH_D = dict()
MATCH_D['('], MATCH_D['{'], MATCH_D['['] = 0, 1, 2
MATCH_D[')'], MATCH_D['}'], MATCH_D[']'] = 0, 1, 2


def check_if_balanced_par(x: str) -> bool:
    """
    We consider only string which are composed of '(', '{', '[' and ')', '}', ']'
    """
    if len(x) < 1:
        return False  # if we have less than one parentheses it is clear that not balanced

    if len(x) % 2 != 0:
        return False  # number of parentheses should be even number

    s = Stack()
    for i in x:
        if i in ('(', '[', '{', ):
            s.push(MATCH_D[i])
        else:  # if i in (')', ']', '}', )
            if s.is_empty():  # prevent error
                return False  # if empty not balanced
            else:
                m_dict_val = s.pop()  # remove bracket
                if MATCH_D[i] != m_dict_val:
                    # it means that we get not expected type of matching bracket
                    # e.g '(' do not match '}'
                    return False

    if s.is_empty():
        return True  # if nothing is Stack - balanced

    return False  # otherwise not balanced
