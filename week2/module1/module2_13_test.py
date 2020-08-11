import module2_13 as tm
import pytest


def test_positive_list():
    pl = tm.PositiveList([1, 2, 3, 4])
    pl.append(5)
    assert pl == [1, 2, 3, 4, 5]

    with pytest.raises(tm.NonPositiveError):
        pl.append(-1)

    with pytest.raises(tm.NonPositiveError):
        pl.append(0)
