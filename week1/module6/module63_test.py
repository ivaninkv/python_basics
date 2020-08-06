import module63 as tm


def test_loglist(capsys):
    ll = tm.LoggableList()
    ll.append(1)
    cap_out, _ = capsys.readouterr()
    assert cap_out.split(':')[3].strip() == '1'

    ll.append(123)
    cap_out, _ = capsys.readouterr()
    assert cap_out.split(':')[3].strip() == '123'

    ll.append('test')
    cap_out, _ = capsys.readouterr()
    assert cap_out.split(':')[3].strip() == 'test'
