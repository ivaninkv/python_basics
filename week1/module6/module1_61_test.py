import module1_61 as tm
import pytest
from io import StringIO


@pytest.mark.skip(reason='need to debug')
def test_integr(monkeypatch, capsys):
    inp = StringIO('''5
                    Obj
                    A : Obj
                    B : A
                    C : A
                    D : B C
                    6
                    A B
                    B D
                    C D
                    D A
                    A D
                    A A''')

    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    captured_stdout, _ = capsys.readouterr()
    assert captured_stdout == 'Yes\nYes\nYes\nNo\nYes\nYes\n'
