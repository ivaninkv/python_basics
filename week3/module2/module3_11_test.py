import module3_11 as tm
from io import StringIO


def test_input_data(monkeypatch):
    inp = StringIO('''ababa\na\nb''')
    monkeypatch.setattr('sys.stdin', inp)
    assert tm.input_data() == ['ababa', 'a', 'b']

    inp = StringIO('''ababa\nb\na''')
    monkeypatch.setattr('sys.stdin', inp)
    assert tm.input_data() == ['ababa', 'b', 'a']


def test_integr(monkeypatch, capsys):
    inp = StringIO('''ababa\na\nb''')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    cap_out, _ = capsys.readouterr()
    assert cap_out == '1\n'

    inp = StringIO('''ababa\nb\na''')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    cap_out, _ = capsys.readouterr()
    assert cap_out == '1\n'

    inp = StringIO('''ababa\nc\nc''')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    cap_out, _ = capsys.readouterr()
    assert cap_out == '0\n'

    inp = StringIO('''ababac\nc\nc''')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    cap_out, _ = capsys.readouterr()
    assert cap_out == 'Impossible\n'
