from Pr_Solv_Algo_DataStr_UsingPython.ch2_simple_class.dice import Dice

d = Dice(6)


def test_dice_repr():
    d2 = Dice(6)
    assert repr(d2) == f"Dice(cur_val={d2.cur_value}, side_number={d2.side_number})"


def test_dice_str():
    d2 = Dice(6)
    assert str(d2) == str(1)


def test_throw():
    assert d.throw() <= 6
    assert d.throw() >= 1
