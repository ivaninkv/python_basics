import module52 as tm


def test_bfr(capsys):
    b = tm.Buffer()
    b.add(1, 2, 3)
    assert b.get_current_part() == [1, 2, 3]
    b.add(4, 5, 6)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == '15\n'
    assert b.get_current_part() == [6]
    b.add(7, 8, 9, 10)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == '40\n'
    assert b.get_current_part() == []
    b.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == '5\n5\n'
    assert b.get_current_part() == [1]
