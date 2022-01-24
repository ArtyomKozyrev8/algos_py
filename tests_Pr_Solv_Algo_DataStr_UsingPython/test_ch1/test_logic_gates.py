from Pr_Solv_Algo_DataStr_UsingPython.ch1_introduction.logic_gates import AndGate, OrGate, NotGate, LogicGate

import pytest

and_g = AndGate("A", True, False)

or_g = OrGate("B", True, False)

not_g = NotGate("C", True)

logic_g = LogicGate("D")


def test_and_get_output():
    assert and_g.get_output() is False


def test_or_get_output():
    assert or_g.get_output() is True


def test_not_get_output():
    assert not_g.get_output() is False


def test_bin_gate_repr():
    assert repr(and_g) == "AndGate(A, True, False)"


def test_unary_gate_repr():
    assert repr(not_g) == "NotGate(C, True)"


def test_logic_gate_get_output():
    with pytest.raises(Exception):
        assert logic_g.get_output()
