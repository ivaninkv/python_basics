import module3_41 as tm
from io import StringIO


def test_integr(monkeypatch, capsys):
    inp = StringIO('''https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html''')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    cap_out, _ = capsys.readouterr()
    assert cap_out == 'Yes\n'
