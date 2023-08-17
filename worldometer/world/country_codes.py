from copy import deepcopy
from dataclasses import dataclass
from typing import List


@dataclass
class CountryCodeData:
    country: str
    calling_code: str
    three_letter_iso: str
    two_letter_iso: str
    three_digit_iso_numeric: str


class CountryCodes:

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(self) -> List[CountryCodeData]:
        return []

    def data(self) -> List[CountryCodeData]:
        return deepcopy(self._data)
