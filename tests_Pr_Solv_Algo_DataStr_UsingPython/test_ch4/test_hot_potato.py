from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.hot_potato_sim import hot_potato


def test_hot_potato():
    assert hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7) == "Susan"
    assert hot_potato(["S"], 7) == "S"
