import module1 as m1


def test_sample():
    assert m1.sum_lst_element([2, 3]) == 5
    assert m1.sum_lst_element([]) == 0
    assert m1.sum_lst_element([-2, -3]) == -5
