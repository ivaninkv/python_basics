import module2_21 as tm
from io import StringIO


def test_integr(monkeypatch, capsys):
    inp = StringIO('''2016 4 20
                      14
                      ''')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    cap_stdout, _ = capsys.readouterr()
    assert cap_stdout == '2016 5 4\n'

    inp = StringIO('''2016 2 20
                      9
                      ''')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    cap_stdout, _ = capsys.readouterr()
    assert cap_stdout == '2016 2 29\n'

    inp = StringIO('''2015 12 31
                      1
                      ''')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    cap_stdout, _ = capsys.readouterr()
    assert cap_stdout == '2016 1 1\n'
