import pytest

from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.linked_list import List, Node


def test_node():
    x = Node(5)
    assert x.next is None
    assert str(x) == "Node(5)"
    x.next = Node(10)
    assert str(x.next) == "Node(10)"


def test_list():
    x = List()
    assert str(x) == "List()"
    assert x.is_empty() is True
    assert x.size() == 0
    x.add(Node(1))
    x.add(Node(2))
    x.add(Node(3))
    assert str(x) == "List(3->2->1->None)"
    assert x.is_empty() is False
    assert x.size() == 3
    x.append(Node(4))
    x.append(Node(5))
    assert str(x) == "List(3->2->1->4->5->None)"
    assert x.is_empty() is False
    assert x.size() == 5
    assert x.search(Node(4)) is True
    assert x.search(Node(6)) is False
    assert x.index(Node(3)) == 0
    assert x.index(Node(2)) == 1
    assert x.index(Node(1)) == 2
    assert x.index(Node(4)) == 3
    assert x.index(Node(5)) == 4
    with pytest.raises(Exception):
        assert x.index(Node(7))
    x.insert(0, Node(6))
    assert str(x) == "List(6->3->2->1->4->5->None)"
    assert x.size() == 6
    x.insert(3, Node(7))
    assert str(x) == "List(6->3->2->7->1->4->5->None)"
    assert x.size() == 7
    x.insert(10, Node(8))
    assert str(x) == "List(6->3->2->7->1->4->5->8->None)"
    assert x.size() == 8
    y = List()
    y.insert(10, Node(10))
    assert str(y) == "List(10->None)"
    assert y.size() == 1
    y.pop()
    assert str(y) == "List()"
    assert y.size() == 0
    assert y.is_empty() is True
    with pytest.raises(Exception):
        assert y.pop()
    with pytest.raises(Exception):
        assert y.remove(Node(9))
    x.pop()
    assert str(x) == "List(6->3->2->7->1->4->5->None)"
    assert x.size() == 7
    x.pop(0)
    assert str(x) == "List(3->2->7->1->4->5->None)"
    assert x.size() == 6
    with pytest.raises(Exception):
        x.pop(10)
    x.pop(3)
    assert str(x) == "List(3->2->7->4->5->None)"
    assert x.size() == 5
    x.pop(4)
    assert str(x) == "List(3->2->7->4->None)"
    assert x.size() == 4
    with pytest.raises(Exception):
        x.remove(Node(10))
    x.remove(Node(7))
    assert str(x) == "List(3->2->4->None)"
    assert x.size() == 3
    x.remove(Node(3))
    assert str(x) == "List(2->4->None)"
    assert x.size() == 2
    x.remove(Node(4))
    assert str(x) == "List(2->None)"
    assert x.size() == 1


def test_list_repr_rec():
    x = List()
    assert List.repr_rec(x._head) == "None"
    x.add(Node(1))
    x.add(Node(2))
    x.add(Node(3))
    assert List.repr_rec(x._head) == "3->2->1->None"


def test_rev_linked_list():
    x = List()
    assert str(x.reverse()) == "List()"
    x.add(Node(1))
    x.add(Node(2))
    x.add(Node(3))
    assert str(x.reverse()) == "List(1->2->3->None)"
    assert str(x.reverse()) == "List(3->2->1->None)"
    y = List()
    y.add(Node(1))
    assert str(y.reverse()) == "List(1->None)"
    assert str(y.reverse()) == "List(1->None)"
