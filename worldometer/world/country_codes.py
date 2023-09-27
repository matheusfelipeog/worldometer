from copy import deepcopy
from dataclasses import dataclass
from typing import List

from worldometer.scraper import get_data_tables


@dataclass
class CountryCodesData:
    country: str
    calling_code: str
    three_letter_iso: str
    two_letter_iso: str
    three_digit_iso_numeric: str

    _table_position = 0


class CountryCodes:

    source_path = '/country-codes'
    new_column_names = (
        'country',
        'calling_code',
        'three_letter_iso',
        'two_letter_iso',
        'three_digit_iso_numeric'
    )

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(self) -> List[CountryCodesData]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                self.new_column_names
            ]
        )
        return [
            CountryCodesData(**data_row)
            for data_row in dts[CountryCodesData._table_position]
        ]

    @property
    def data(self) -> List[CountryCodesData]:
        return deepcopy(self._data)
