from project import get_country, get_name, get_opponents


def test_get_name():
    assert get_name('  federico  ') == 'Federico'
    assert get_name('federico') == 'Federico'
    assert get_name('FEDERICO') == 'Federico'
    assert get_name('FeDerICo') == 'Federico'
    assert get_name('fedeRIco123') == 'Federico123'
    assert get_name('john_doe') == 'John_doe'
    assert get_name('john.DOE') == 'John.doe'


def test_get_country():
    assert get_country('ARGENtina') == 'Argentina'
    assert get_country('ar') == 'Argentina'
    assert get_country('aRg') == 'Argentina'
    assert get_country('UNITED states') == 'United States'
    assert get_country('us') == 'United States'
    assert get_country('usa') == 'United States'
    assert get_country('AUSTRIA') == 'Austria'
    assert get_country('AUT') == 'Austria'
    assert get_country('at') == 'Austria'


def test_get_opponents():
    assert len(get_opponents(2)) == 1
    assert len(get_opponents(4)) == 3
    assert len(get_opponents(8)) == 7