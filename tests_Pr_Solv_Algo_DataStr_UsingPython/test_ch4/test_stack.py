from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.stack import Stack

import pytest


def test_stack():
    x = Stack()
    assert x.size() == 0
    x.push(0)
    assert x.size() == 1
    x.push(1)
    x.push(2)
    x.push(3)
    assert x.size() == 4
    assert x.pop() == 3
    assert x.pop() == 2
    assert x.size() == 2
    assert x.peek() == 1
    assert x.is_empty() is False
    assert x.pop() == 1
    assert x.pop() == 0
    assert x.is_empty() is True
    with pytest.raises(Exception):
        x.pop()
