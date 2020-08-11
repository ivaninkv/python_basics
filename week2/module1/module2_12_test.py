import module2_12 as tm
from io import StringIO


def test_input(monkeypatch):
    inp = StringIO('''2
                    ArithmeticError
                    ZeroDivisionError : ArithmeticError AssertError
                    1
                    ZeroDivisionError''')
    monkeypatch.setattr('sys.stdin', inp)
    inp_ex, req_lst = tm.input_data()
    assert inp_ex == {'ArithmeticError': None,
                      'ZeroDivisionError': set(['ArithmeticError',
                                                'AssertError']),
                      'AssertError': None}
    assert req_lst == ['ZeroDivisionError']

    inp = StringIO('''4
                    ArithmeticError
                    ZeroDivisionError : ArithmeticError
                    OSError
                    FileNotFoundError : OSError
                    4
                    ZeroDivisionError
                    OSError
                    ArithmeticError
                    FileNotFoundError''')
    monkeypatch.setattr('sys.stdin', inp)
    inp_ex, req_lst = tm.input_data()
    assert inp_ex == {'ArithmeticError': None,
                      'ZeroDivisionError': set(['ArithmeticError']),
                      'OSError': None,
                      'FileNotFoundError': set(['OSError'])}
    assert req_lst == ['ZeroDivisionError', 'OSError',
                       'ArithmeticError', 'FileNotFoundError']

    inp = StringIO('''4
                    BaseException
                    Exception : BaseException
                    LookupError : Exception
                    KeyError : LookupError
                    2
                    BaseException
                    KeyError
                    ''')
    monkeypatch.setattr('sys.stdin', inp)
    inp_ex, req_lst = tm.input_data()
    assert inp_ex == {'BaseException': None,
                      'Exception': set(['BaseException']),
                      'LookupError': set(['Exception']),
                      'KeyError': set(['LookupError'])}
    assert req_lst == ['BaseException', 'KeyError']


def test_parents():
    assert tm.get_parents({'ArithmeticError': None,
                           'ZeroDivisionError': set(['ArithmeticError'])},
                          'ZeroDivisionError') == set(['ArithmeticError'])
    assert tm.get_parents({'ArithmeticError': None,
                           'ZeroDivisionError': set(['ArithmeticError']),
                           'OSError': None,
                           'FileNotFoundError': set(['OSError'])},
                          'FileNotFoundError') == set(['OSError'])
    assert tm.get_parents({'BaseException': None,
                           'Exception': set(['BaseException']),
                           'LookupError': set(['Exception']),
                           'KeyError': set(['LookupError'])},
                          'KeyError') == set(['LookupError',
                                             'Exception', 'BaseException'])


def test_intersect():
    assert tm.is_intersect(set([1, 2, 3]), set([3, 4, 5])) is True
    assert tm.is_intersect(set([1, 2, 3]), set([6, 4, 5])) is False
    assert tm.is_intersect(set(['1', 2, 3]), set([6, 4, 5])) is False


def test_integrated(monkeypatch, capsys):
    inp = StringIO('''4
                    ArithmeticError
                    ZeroDivisionError : ArithmeticError
                    OSError
                    FileNotFoundError : OSError
                    4
                    ZeroDivisionError
                    OSError
                    ArithmeticError
                    FileNotFoundError''')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    captured_stdout, _ = capsys.readouterr()
    assert captured_stdout == 'FileNotFoundError\n'

    inp = StringIO('''4
                    winter
                    is
                    coming
                    OMG : winter is coming
                    4
                    winter
                    is
                    coming
                    OMG''')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    captured_stdout, _ = capsys.readouterr()
    assert captured_stdout == 'OMG\n'

    inp = StringIO('''4
                    BaseException
                    Exception : BaseException
                    LookupError : Exception
                    KeyError : LookupError
                    2
                    BaseException
                    KeyError
                    ''')
    monkeypatch.setattr('sys.stdin', inp)
    tm.main()
    captured_stdout, _ = capsys.readouterr()
    assert captured_stdout == 'KeyError\n'
