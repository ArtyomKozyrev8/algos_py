from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.infix_to_prefix import convert_infix_to_prefix


def test_convert_infix_to_prefix():
    assert convert_infix_to_prefix("") == ""
    assert convert_infix_to_prefix("A") == "A"
    assert convert_infix_to_prefix("A+B") == "AB+"
    assert convert_infix_to_prefix("A+B*C") == "ABC*+"
    assert convert_infix_to_prefix("(A+B)*C") == "AB+C*"
    assert convert_infix_to_prefix("A+B*C+D") == "ABC*+D+"
    assert convert_infix_to_prefix("(A+B)*(C+D)") == "AB+CD+*"
    assert convert_infix_to_prefix("A*B+C*D") == "AB*CD*+"
    assert convert_infix_to_prefix("A+B+C+D") == "AB+C+D+"
    assert convert_infix_to_prefix("(A+B+C)*D") == "AB+C+D*"
    assert convert_infix_to_prefix("(A+B*C*D)+F") == "ABC*D*+F+"
    assert convert_infix_to_prefix("A+B*C*D+F") == "ABC*D*+F+"
    assert convert_infix_to_prefix("A+B*C*D") == "ABC*D*+"

