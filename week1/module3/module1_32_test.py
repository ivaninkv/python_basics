import module1_32 as tm  # tested module


def test_int():
    assert tm.C(3, 2) == 3
    assert tm.C(10, 5) == 252
    assert tm.C(3, 0) == 1
    assert tm.C(10, 0) == 1
