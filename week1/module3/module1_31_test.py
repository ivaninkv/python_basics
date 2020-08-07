import module1_31 as m3


def test_int():
    assert m3.closest_mod_5(5) == 5
    assert m3.closest_mod_5(6) == 10
    assert m3.closest_mod_5(11) == 15
    assert m3.closest_mod_5(0) == 0
