import pytest

from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.ordered_linked_list import OrderedList, Node


def test_add():
    x = OrderedList()
    assert str(x) == "OrderedList()"
    assert x.is_empty() is True
    assert x.size() == 0
    x.add(Node(4))
    x.add(Node(2))
    x.add(Node(3))
    x.add(Node(1))
    assert str(x) == "OrderedList(1, 2, 3, 4)"
    assert x.is_empty() is False
    assert x.size() == 4
    x.add(Node(5))
    assert str(x) == "OrderedList(1, 2, 3, 4, 5)"
    assert x.is_empty() is False
    assert x.size() == 5


def test_remove():
    x = OrderedList()
    with pytest.raises(Exception):
        x.remove(Node(10))
    x.add(Node(4))
    x.add(Node(2))
    x.add(Node(3))
    x.add(Node(1))
    x.add(Node(5))
    with pytest.raises(Exception):
        x.remove(Node(11))
    x.remove(Node(1))
    assert str(x) == "OrderedList(2, 3, 4, 5)"
    assert x.is_empty() is False
    assert x.size() == 4
    x.add(Node(10))
    with pytest.raises(Exception):
        x.remove(Node(8))
    x.remove(Node(5))
    assert str(x) == "OrderedList(2, 3, 4, 10)"
    assert x.is_empty() is False
    assert x.size() == 4
    x.remove(Node(10))
    assert str(x) == "OrderedList(2, 3, 4)"
    assert x.is_empty() is False
    assert x.size() == 3


def test_index():
    x = OrderedList()
    with pytest.raises(Exception):
        x.index(Node(10))

    x.add(Node(10))
    x.add(Node(8))
    x.add(Node(4))
    x.add(Node(2))
    x.add(Node(5))
    assert str(x) == "OrderedList(2, 4, 5, 8, 10)"
    assert x.is_empty() is False
    assert x.size() == 5
    assert x.index(Node(2)) == 0
    with pytest.raises(Exception):
        x.index(Node(7))
    assert x.index(Node(10)) == 4
    with pytest.raises(Exception):
        x.index(Node(11))
    assert x.index(Node(5)) == 2


def test_search():
    x = OrderedList()
    assert x.search(Node(10)) is False

    x.add(Node(10))
    x.add(Node(8))
    x.add(Node(4))
    x.add(Node(2))
    x.add(Node(5))
    assert str(x) == "OrderedList(2, 4, 5, 8, 10)"
    assert x.is_empty() is False
    assert x.size() == 5
    assert x.search(Node(2)) is True
    assert x.search(Node(7)) is False
    assert x.search(Node(10)) is True
    assert x.search(Node(11)) is False


def test_pop():
    x = OrderedList()
    with pytest.raises(Exception):
        assert x.pop() is False
    with pytest.raises(Exception):
        assert x.pop(5) is False
    x.add(Node(10))
    x.add(Node(8))
    x.add(Node(4))
    x.add(Node(2))
    x.add(Node(5))
    x.add(Node(6))
    x.add(Node(14))
    assert str(x) == "OrderedList(2, 4, 5, 6, 8, 10, 14)"
    assert x.pop() == 14
    assert x.pop(0) == 2
    assert str(x) == "OrderedList(4, 5, 6, 8, 10)"
    assert x.size() == 5
    with pytest.raises(Exception):
        assert x.pop(11)
    assert x.pop(2) == 6
    assert str(x) == "OrderedList(4, 5, 8, 10)"
    assert x.size() == 4

    y = OrderedList()
    y.add(Node(1))
    assert y.pop() == 1
    assert str(y) == "OrderedList()"
    assert y.size() == 0
    with pytest.raises(Exception):
        assert y.pop()
