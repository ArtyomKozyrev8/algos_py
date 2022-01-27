from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.queue import Queue

import pytest


def test_queue():
    x = Queue()
    assert x.size() == 0
    x.enqueue(0)
    assert x.size() == 1
    x.enqueue(1)
    x.enqueue(2)
    x.enqueue(3)
    assert repr(x) == f'Queue([3, 2, 1, 0])'
    assert x.size() == 4
    assert x.dequeue() == 0
    assert x.dequeue() == 1
    assert x.size() == 2
    assert x.is_empty() is False
    assert x.dequeue() == 2
    assert x.dequeue() == 3
    assert x.is_empty() is True
    with pytest.raises(Exception):
        x.dequeue()
