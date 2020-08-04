import module4 as tm
from io import StringIO


def test_integr(monkeypatch, capsys):
    inp = StringIO('''9
                    add global a
                    create foo global
                    add foo b
                    get foo a
                    get foo c
                    create bar foo
                    add bar a
                    get bar a
                    get bar b''')

    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == 'global\nNone\nbar\nfoo\n'

    inp = StringIO('''5
                    create foo global
                    add foo b
                    create foo2 foo
                    create foo3 foo2
                    get foo3 b''')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == 'foo\n'
