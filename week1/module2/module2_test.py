import module2 as m2


def test_int_list():
    assert m2.uniq_elem([1, 2, 3, 4, 5, 1, 2]) == 5
    assert m2.uniq_elem([3, 3, 3, 3, 2]) == 2
    assert m2.uniq_elem([1, 2, 3, 50, 50, 3]) == 4


def test_str_list():
    assert m2.uniq_elem(['one', 'two', 'three']) == 3
    assert m2.uniq_elem(['one', 'two', 'three', 'one']) == 3
    assert m2.uniq_elem(['one', 'two', 'three', 'one', 'four']) == 4


def test_mix_list():
    assert m2.uniq_elem([1, 2, 1, 2, 3, [1], [1]]) == 5
    assert m2.uniq_elem([1, 2, 'three', ['four']]) == 4
