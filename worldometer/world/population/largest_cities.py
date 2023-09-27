from copy import deepcopy
from dataclasses import dataclass
from typing import List

from worldometer.scraper import get_data_tables


@dataclass
class LargestCitiesData:
    rank: int
    urban_area: str
    population_estimate: str
    country: str
    land_area: int
    density: int

    _table_position = 0


class LargestCities:

    source_path = '/population/largest-cities-in-the-world'
    new_column_names = (
        'rank',
        'urban_area',
        'population_estimate',
        'country',
        'land_area',
        'density'
    )

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(self) -> List[LargestCitiesData]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                self.new_column_names
            ],
            attrs=None
        )
        return [
            LargestCitiesData(**data_row)
            for data_row in dts[LargestCitiesData._table_position]
        ]

    @property
    def data(self) -> List[LargestCitiesData]:
        return deepcopy(self._data)
