import pytest

from worldometer.scraper.utils import make_url


@pytest.fixture
def base_url():
    return 'https://www.example.com'


def test_make_url(base_url):
    url = make_url(base_url)

    assert url == base_url


@pytest.mark.parametrize(
    'path_url',
    ['/', '/a', '/a/b', '/a/b/', '/a1', '/a2/', '/a?arg=1']
)
def test_make_url_with_path_url_param(base_url, path_url):
    url = make_url(base_url, path_url)

    expected_url = base_url + path_url

    assert url == expected_url


@pytest.mark.parametrize(
    'path_url',
    ['', 'a', 'a/', 'a/b/', 'a?arg=1']
)
def test_make_url_with_invalid_path_url_param(base_url, path_url):
    url = make_url(base_url, path_url)

    assert url == base_url
