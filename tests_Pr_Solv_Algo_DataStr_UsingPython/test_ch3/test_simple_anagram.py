from Pr_Solv_Algo_DataStr_UsingPython.ch3_analysis.simple_anagram import check_simple_anagram


def test_check_simple_anagram():
    assert check_simple_anagram("2", "222") is False
    assert check_simple_anagram("abccd", "aaaab") is False
    assert check_simple_anagram("abcde", "bcdef") is False
    assert check_simple_anagram("abcd", "dacb") is True
