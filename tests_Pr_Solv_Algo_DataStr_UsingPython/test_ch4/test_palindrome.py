from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.palindrome import check_palindrome


def test_check_if_balanced_par():
    assert check_palindrome('') is True
    assert check_palindrome('x') is True
    assert check_palindrome('xx') is True
    assert check_palindrome('yxy') is True
    assert check_palindrome('lsdkjfskf') is False
    assert check_palindrome('radar') is True