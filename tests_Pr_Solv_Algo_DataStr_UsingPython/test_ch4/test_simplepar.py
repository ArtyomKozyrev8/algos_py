from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.simple_parentheses import check_if_balanced_par


def test_check_if_balanced_par():
    assert check_if_balanced_par('') is False
    assert check_if_balanced_par('(') is False
    assert check_if_balanced_par('(()') is False
    assert check_if_balanced_par('((()))') is True
    assert check_if_balanced_par('((((()))()') is False
    assert check_if_balanced_par('((()))(())()()') is True
    assert check_if_balanced_par('((()))(())()())(') is False
