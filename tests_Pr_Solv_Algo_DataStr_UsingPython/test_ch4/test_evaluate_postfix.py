from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.evaluate_postfix import evaluate_postfix


def test_evaluate_postfix():
    assert evaluate_postfix("10 3 5 * 16 4 - / +") == 11.25
    assert evaluate_postfix("17 10 + 3 * 9 /") == 9
    assert evaluate_postfix("4 5 6 * +") == 34
    assert evaluate_postfix("10") == 10
