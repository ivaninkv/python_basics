import module2_31 as tm


def test_mf():
    data = [i for i in range(31)]
    mf = tm.multifilter(data, lambda x: x % 2 == 0,
                        lambda x: x % 3 == 0, lambda x: x % 5 == 0)
    assert list(mf) == [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15,
                        16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

    mf = tm.multifilter(data, lambda x: x % 2 == 0, lambda x: x % 3 == 0,
                        lambda x: x % 5 == 0, judge=tm.multifilter.judge_half)
    assert list(mf) == [0, 6, 10, 12, 15, 18, 20, 24, 30]

    mf = tm.multifilter(data, lambda x: x % 2 == 0, lambda x: x % 3 == 0,
                        lambda x: x % 5 == 0, judge=tm.multifilter.judge_all)
    assert list(mf) == [0, 30]
