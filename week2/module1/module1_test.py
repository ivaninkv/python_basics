import pytest
import module1 as tm


def test_foo(capsys):
    with pytest.raises(ZeroDivisionError):
        tm.foo(1)
    tm.main(1)
    cap_out, _ = capsys.readouterr()
    assert cap_out == 'ZeroDivisionError\n'

    with pytest.raises(ArithmeticError):
        tm.foo(2)
    tm.main(2)
    cap_out, _ = capsys.readouterr()
    assert cap_out == 'ArithmeticError\n'

    with pytest.raises(AssertionError):
        tm.foo(3)
    tm.main(3)
    cap_out, _ = capsys.readouterr()
    assert cap_out == 'AssertionError\n'
