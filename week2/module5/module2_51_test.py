import module2_51 as tm


def test_mod_checjer():
    mod_3 = tm.mod_checker(3)
    assert mod_3(3) is True
    assert mod_3(4) is False

    mod_3_1 = tm.mod_checker(3, 1)
    assert mod_3_1(3) is False
    assert mod_3_1(4) is True
