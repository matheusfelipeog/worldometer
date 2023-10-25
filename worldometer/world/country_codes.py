from copy import deepcopy
from dataclasses import dataclass
from typing import List

from worldometer.scraper import get_data_tables


@dataclass
class CountryCodesData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    country: str
    calling_code: str
    three_letter_iso: str
    two_letter_iso: str
    three_digit_iso_numeric: str
    """
    country: str
    calling_code: str
    three_letter_iso: str
    two_letter_iso: str
    three_digit_iso_numeric: str

    _table_position = 0


class CountryCodes:
    """Represents the data table of some codes used by each country.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original table.

    Notes
    -----
    Check the source table in
    `Worldometers Country Codes <https://www.worldometers.info/country-codes/>`_.
    """
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
        """Get a list of all the data from the table.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data)
