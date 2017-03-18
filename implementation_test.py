import pytest

from implementation import IntBin, StringBin


def test_integers():

    integers = IntBin(1, 5, 2, 7, 9, 9, 4)

    assert integers.search(5) == 4
    assert integers.search(1) == 0
    assert integers.search(9) == 5
    assert (4 in integers) == True
    assert (10 in integers) == False

    try:
        IntBin(1, 3, 5, 'a')
    except TypeError:
        pass
    else:
        raise ValueError('Тут должно быть исключение TypeError, а его нет!')


def test_strings():

    strings = StringBin(['a', 'mama', 'papa', 'papa', 'vasa', 'kola'])

    assert strings.search('mama') == 2
    assert strings.search('a') == 0
    assert strings.search('papa') == 3
    assert ('vasa' in strings) == True
    assert ('olala' in strings) == False

    try:
        StringBin(('a', 'b', {'a': 'b'}))
    except TypeError:
        pass
    else:
        raise ValueError('Тут должно быть исключение TypeError, а его нет!')
