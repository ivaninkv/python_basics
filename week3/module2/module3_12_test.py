import module3_12 as tm
from io import StringIO


def test_input_data(monkeypatch):
    inp = StringIO('abababa\naba')
    monkeypatch.setattr('sys.stdin', inp)
    s, t = tm.input_data()
    assert s, t == ['abababa' 'aba']

    inp = StringIO('abababa\nabc')
    monkeypatch.setattr('sys.stdin', inp)
    s, t = tm.input_data()
    assert s, t == ['abababa' 'abc']


def test_substr_count():
    assert tm.substr_count('abababa', 'aba') == 3
    assert tm.substr_count('abababa', 'abc') == 0
    assert tm.substr_count('abc', 'abc') == 1
    assert tm.substr_count('aaaaa', 'a') == 5


def test_integr(monkeypatch, capsys):
    inp = StringIO('abababa\naba')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    cap_out, _ = capsys.readouterr()
    assert cap_out == '3\n'

    inp = StringIO('abababa\nabc')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    cap_out, _ = capsys.readouterr()
    assert cap_out == '0\n'

    inp = StringIO('aaaaa\na')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    cap_out, _ = capsys.readouterr()
    assert cap_out == '5\n'
