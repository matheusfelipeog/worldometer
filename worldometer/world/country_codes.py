from copy import deepcopy
from dataclasses import dataclass
from typing import List

from worldometer.scraper.controller import get_data_tables


@dataclass
class CountryCodesData:
    country: str
    calling_code: str
    three_letter_iso: str
    two_letter_iso: str
    three_digit_iso_numeric: str


class CountryCodes:

    source_path = '/country-codes'
    table_position = 0
    column_names = (
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
                self.column_names
            ]
        )
        return [
            CountryCodesData(**data_line)
            for data_line in dts[self.table_position]
        ]

    @property
    def data(self) -> List[CountryCodesData]:
        return deepcopy(self._data)
