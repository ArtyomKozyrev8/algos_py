import pytest

from Pr_Solv_Algo_DataStr_UsingPython.ch6_sorting_searching.hashing import HashTable


def test_simple():
    x = HashTable(11)
    assert str(x) == f"HashTable({[(None, None)]*11})"
    assert len(x) == 0
    x[26] = "a"
    temp = [(None, None)] * 11
    temp[4] = (26, "a")
    assert str(x) == f"HashTable({temp})"
    assert len(x) == 1
    x[29] = "b"
    temp[7] = (29, "b")
    assert str(x) == f"HashTable({temp})"
    assert len(x) == 2
    assert (5 in x) is False
    assert (26 in x) is True
    del x[26]
    temp[4] = (None, None)
    assert str(x) == f"HashTable({temp})"
    assert len(x) == 1


def test_set_ger_del():
    x = HashTable(5)
    assert str(x) == f"HashTable({[(None, None)]*5})"
    assert len(x) == 0
    x[26] = "a"
    assert len(x) == 1
    assert str(x) == f"HashTable([(None, None), (26, 'a'), (None, None), (None, None), (None, None)])"
    x[34] = "b"
    assert len(x) == 2
    assert str(x) == f"HashTable([(None, None), (26, 'a'), (None, None), (None, None), (34, 'b')])"
    x[39] = "c"
    assert len(x) == 3
    assert str(x) == f"HashTable([(39, 'c'), (26, 'a'), (None, None), (None, None), (34, 'b')])"
    assert x[99] is None
    x[99] = "d"
    assert len(x) == 4
    assert str(x) == f"HashTable([(39, 'c'), (26, 'a'), (99, 'd'), (None, None), (34, 'b')])"
    x[103] = "e"
    assert len(x) == 5
    assert str(x) == f"HashTable([(39, 'c'), (26, 'a'), (99, 'd'), (103, 'e'), (34, 'b')])"
    with pytest.raises(Exception):
        x[108] = "a2"

    assert x[108] is None

    x[103] = "e2"
    assert len(x) == 5
    assert str(x) == f"HashTable([(39, 'c'), (26, 'a'), (99, 'd'), (103, 'e2'), (34, 'b')])"

    x[99] = "d2"
    assert len(x) == 5
    assert str(x) == f"HashTable([(39, 'c'), (26, 'a'), (99, 'd2'), (103, 'e2'), (34, 'b')])"

    del x[1044]
    assert len(x) == 5
    assert str(x) == f"HashTable([(39, 'c'), (26, 'a'), (99, 'd2'), (103, 'e2'), (34, 'b')])"

    del x[103]
    assert len(x) == 4
    assert str(x) == f"HashTable([(39, 'c'), (26, 'a'), (99, 'd2'), (None, None), (34, 'b')])"

    del x[99]
    assert len(x) == 3
    assert str(x) == f"HashTable([(39, 'c'), (26, 'a'), (None, None), (None, None), (34, 'b')])"

    del x[99]
    assert len(x) == 3
    assert str(x) == f"HashTable([(39, 'c'), (26, 'a'), (None, None), (None, None), (34, 'b')])"

    x[108] = "a2"
    assert len(x) == 4
    assert str(x) == f"HashTable([(39, 'c'), (26, 'a'), (None, None), (108, 'a2'), (34, 'b')])"



