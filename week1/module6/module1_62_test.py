import module1_62 as tm


def test_int_list():
    es = tm.ExtendedStack([1, 2, 3])
    es.sum()
    assert es == [1, 5]
    es.sub()
    assert es == [4]
    es.extend([1, 2, 3, 4, 5])
    es.mul()
    assert es == [4, 1, 2, 3, 20]
    es.div()
    assert es == [4, 1, 2, 6]
