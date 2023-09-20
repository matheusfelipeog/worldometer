from copy import deepcopy
from dataclasses import dataclass
from typing import List

from worldometer.scraper import get_data_tables


@dataclass
class LargestCountriesData:
    position: int
    country: str
    total_area_km2: int
    total_area_mi2: int
    land_area_km2: int
    land_area_mi2: int
    percentage_of_world_landmass: str

    _table_position = 0


class LargestCountries:

    source_path = '/geography/largest-countries-in-the-world'
    new_column_names = (
        'position',
        'country',
        'total_area_km2',
        'total_area_mi2',
        'land_area_km2',
        'land_area_mi2',
        'percentage_of_world_landmass'
    )

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(self) -> List[LargestCountriesData]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                self.new_column_names
            ]
        )
        return [
            LargestCountriesData(**data_row)
            for data_row in dts[LargestCountriesData._table_position]
        ]

    @property
    def data(self) -> List[LargestCountriesData]:
        return deepcopy(self._data)
