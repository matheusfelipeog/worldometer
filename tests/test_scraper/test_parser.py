import pytest

from worldometer.scraper.parser import (
    get_rts_counters_only_with_last_value_key,
    get_html_tables_data
)
from worldometer.scraper.exceptions import (
    ColumnNamesLengthError
)


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


@pytest.fixture
def fake_html():
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML to Tests</title>
        </head>
        <body>
            <table class="table">
                <thead>
                    <tr>
                        <th>A</th>
                        <th>B</th>
                        <th>C</th>
                        <th>D</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>test</td>
                        <td>1</td>
                        <td>1.0</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>test</td>
                        <td>1</td>
                        <td>1.0</td>
                        <td></td>
                    </tr>
                </tbody>
            </table>

            <table>
                <thead>
                    <tr>
                        <th>A</th>
                        <th>B</th>
                        <th>C</th>
                        <th>D</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>test</td>
                        <td>1</td>
                        <td>1.0</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>test</td>
                        <td>1</td>
                        <td>1.0</td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
        </body>
        </html>
"""


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


def test_get_html_tables_data(fake_html: str):
    num_expected_tables = 2
    attrs = None
    new_column_names = [('A1', 'B1', 'C1', 'D1'), ('A2', 'B2', 'C2', 'D2')]

    data = get_html_tables_data(
        html=fake_html,
        attrs=attrs,
        new_column_names=new_column_names
    )

    assert isinstance(data, list)
    assert len(data) == num_expected_tables

    all_table_data = [td for td in data]
    assert all(
        isinstance(td, list) for td in all_table_data
    ), 'Table with wrong type. Each data table must be a list.'

    data_rows = [
        data_row
        for td in all_table_data
        for data_row in td
    ]
    assert all(
        isinstance(dr, dict)
        for dr in data_rows
    ), 'Data row with wrong type. Each row of data must be a dict.'

    assert all(
        tuple(dr.keys()) in new_column_names
        for dr in data_rows
    ), 'The column names are wrong. They are expected to match the column names passed.'

    data_rows_values = [
        value
        for dr in data_rows
        for value in dr.values()
    ]
    assert all(
        isinstance(value, (int, float, str))
        for value in data_rows_values
    ), 'The column value is not of a supported type. It is expected to be int, float or str.'


def test_get_html_tables_data_with_attrs(fake_html: str):
    num_expected_tables = 1
    attrs = {'class': 'table'}
    new_column_names = [('A1', 'B1', 'C1', 'D1')]

    data = get_html_tables_data(
        html=fake_html,
        attrs=attrs,
        new_column_names=new_column_names  # type: ignore
    )

    assert isinstance(data, list)
    assert len(data) == num_expected_tables

    table_data = data[0]
    assert isinstance(table_data, list)

    assert all(
        isinstance(data_row, dict)
        for data_row in table_data
    ), 'Data row with wrong type. Each row of data must be a dict.'

    assert all(
        tuple(dr.keys()) in new_column_names
        for dr in table_data
    ), 'The column names are wrong. They are expected to match the column names passed.'

    data_rows_values = [
        value
        for dr in table_data
        for value in dr.values()
    ]
    assert all(
        isinstance(value, (int, float, str))
        for value in data_rows_values
    ), 'The column value is not of a supported type. It is expected to be int, float or str.'


def test_get_html_tables_data_with_wrong_length_of_new_column_names(fake_html):

    with pytest.raises(ColumnNamesLengthError):
        get_html_tables_data(fake_html, attrs=None, new_column_names=[])

        get_html_tables_data(fake_html, attrs=None, new_column_names=[('A1', 'B1', 'C1', 'D1')])

        get_html_tables_data(fake_html, attrs=None, new_column_names=[('A1',), ('A2',), ('A3',)])

        get_html_tables_data(fake_html, attrs=None, new_column_names=[tuple(), tuple()])

        get_html_tables_data(fake_html, attrs=None, new_column_names=[('A1', 'B1'), ('A2', 'B2')])

        get_html_tables_data(
            fake_html,
            attrs=None,
            new_column_names=[('A1', 'B1', 'C1', 'D1', 'E1'), ('A2', 'B2', 'C2', 'D2', 'E2')]
        )
