from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.deque import Dequeue

import pytest


def test_stack():
    x = Dequeue()
    assert x.size() == 0
    x.add_front(0)
    assert x.size() == 1
    x.add_front(1)
    x.add_front(2)
    x.add_rear(3)
    x.add_rear(4)
    assert repr(x) == f'Dequeue([4, 3, 0, 1, 2])'
    assert x.size() == 5
    assert x.remove_front() == 2
    assert x.remove_front() == 1
    assert repr(x) == f'Dequeue([4, 3, 0])'
    assert x.size() == 3
    assert x.is_empty() is False
    assert x.remove_rear() == 4
    assert x.remove_rear() == 3
    assert x.remove_front() == 0
    assert x.size() == 0
    assert x.is_empty() is True
    with pytest.raises(Exception):
        x.remove_front()
    with pytest.raises(Exception):
        x.remove_rear()
