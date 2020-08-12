import module2_32 as tm
import itertools


def test_primes():
    assert list(itertools.takewhile(lambda x: x <= 31,
                tm.primes())) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
