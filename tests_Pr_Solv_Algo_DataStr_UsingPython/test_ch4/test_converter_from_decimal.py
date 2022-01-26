from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.converter_from_decimal import convert_from_decimal


def test_convert_from_decimal():
    assert convert_from_decimal(15, base=16) == 'F'
    assert convert_from_decimal(42, base=2) == '101010'
    assert convert_from_decimal(25, base=2) == '11001'
    assert convert_from_decimal(25, base=16) == '19'
    assert convert_from_decimal(0, base=2) == '0'
    assert convert_from_decimal(1, base=2) == '1'
    assert convert_from_decimal(2, base=2) == '10'
