import pytest

from worldometer.scraper.parser import get_rts_counters_only_with_last_value_key


@pytest.fixture
def fake_rts_counters_object():
    return {
        'a': {
            'k1': {},
            'k2': 'test',
            'last_value': 1
        },
        'b': {
            'k1': {},
            'k2': 'test',
            'last_value': 1.0
        },
        'c': {
            'k1': {},
            'k2': 'test',
            'last_value': None
        }
    }


def test_get_rts_counters_only_with_last_value_key(fake_rts_counters_object: dict):

    rts_counters = get_rts_counters_only_with_last_value_key(fake_rts_counters_object)

    assert isinstance(rts_counters, dict)
    assert set(rts_counters.keys()) == set(fake_rts_counters_object.keys())
    assert all(
        isinstance(v, (int, float, type(None)))
        for v in rts_counters.values()
    )


def test_empty_rts_counters_object_passed():
    empty_rts_counters = {}

    rts_counters = get_rts_counters_only_with_last_value_key(empty_rts_counters)

    assert isinstance(rts_counters, dict)
    assert len(rts_counters) == 0
