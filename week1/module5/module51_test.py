import module51 as tm


def test_money_box():
    mb = tm.MoneyBox(0)
    assert mb.can_add(0) is True
    assert mb.can_add(1) is False

    mb = tm.MoneyBox(10)
    assert mb.can_add(0) is True
    assert mb.can_add(1) is True
    mb.add(5)
    assert mb.coins == 5
