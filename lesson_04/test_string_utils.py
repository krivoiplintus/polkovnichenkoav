import pytest
from StringUtils import StringUtils


@pytest.mark.parametrize('str, result', [
    ('тест', 'Тест'),
    ('123', '123'),
    ('тест 123', 'Тест 123'),
    ('', ''),
    (' ', ' '),
    (None, None)
    ])
def test_capitilize(str, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(str)
    assert res == result


@pytest.mark.parametrize('str, symbol', [
    ('тест', 'т'),
    ('123', '1'),
    ('Тест 123', '4'),
    ('', ''),
    (' ', ' '),
    (None, None)
    ])
def test_contains(str, symbol):
    stringUtils = StringUtils()
    res = stringUtils.contains(str, symbol)
    assert res == True


@pytest.mark.parametrize('str, symbol, newstr', [
    ('тест', 'т', 'ес'),
    ('123', '1', '23'),
    ('Тест 123', 'н', 'Теcт 123'),
    ('', '', ''),
    (' ', ' ', ''),
    (None, None, None)
    ])
def test_delete_symbol(str, symbol, newstr):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(str, symbol)
    assert res == newstr


@pytest.mark.parametrize('str, symbol', [
    ('тест', 'т'),
    ('123', '3'),
    ('Тест 123', '4'),
    ('', ''),
    (' ', ' '),
    (None, None)
    ])
def test_end_with(str, symbol):
    stringUtils = StringUtils()
    res = stringUtils.end_with(str, symbol)
    assert res == True


@pytest.mark.parametrize('str', [
    ('тест'),
    ('123'),
    ('Тест 123'),
    (''),
    (' '),
    (None)
    ])
def test_is_empty(str):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(str)
    assert res == False


@pytest.mark.parametrize('lst, joiner, str', [
    (["Т", "е", "с", "т"], '-', 'Т-е-с-т'),
    ([1, 2, 3, 4, 5], ', ', '1, 2, 3, 4, 5'),
    (["Т", 1], ': ', 'Т: 1'),
    ([], '.', ''),
    ('     ', ',', ' , , , , '),
    ([None], None, None)
    ])
def test_list_to_string(lst, joiner, str):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(lst, joiner)
    assert res == str


@pytest.mark.parametrize('str, symbol', [
    ('тест', 'т'),
    ('123', '1'),
    ('Тест 123', 'т'),
    ('', ''),
    (' ', ' '),
    (None, None)
    ])
def test_starts_with(str, symbol):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(str, symbol)
    assert res == True


@pytest.mark.parametrize('str, delimeter, lst', [
    ('т-е-с-т', '-', ['т', 'е', 'с', 'т']),
    ('1,2,3,4,5', ',', ['1', '2', '3', '4', '5']),
    ('', '', []),
    (' , , , , ', ',', [' ', ' ', ' ', ' ', ' ']),
    (None, None, [None])
    ])
def test_to_list(str, delimeter, lst):
    stringUtils = StringUtils()
    res = stringUtils.to_list(str, delimeter)
    assert res == lst


@pytest.mark.parametrize('str, nstr', [
    (' тест', 'тест'),
    (' 123', '123'),
    (' Тест 123', 'Тест 123'),
    ('', ''),
    (' ', ''),
    (None, None)
    ])
def test_trim(str, nstr):
    stringUtils = StringUtils()
    res = stringUtils.trim(str)
    assert res == nstr
