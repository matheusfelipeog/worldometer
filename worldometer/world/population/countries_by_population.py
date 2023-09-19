from copy import deepcopy
from dataclasses import dataclass
from typing import List

from worldometer.scraper import get_data_tables


@dataclass
class CountriesByPopulationData:
    position: int
    country: str
    population: int
    yearly_change: str
    net_change: int
    density: int
    land_area: int
    migrants: int
    fertility_rate: float
    median_age: float
    urban_population: str
    world_share: str

    _table_position = 0


class CountriesByPopulation:

    source_path = '/world-population/population-by-country'
    new_column_names = (
        'position',
        'country',
        'population',
        'yearly_change',
        'net_change',
        'density',
        'land_area',
        'migrants',
        'fertility_rate',
        'median_age',
        'urban_population',
        'world_share'
    )

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(self) -> List[CountriesByPopulationData]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                self.new_column_names
            ]
        )
        return [
            CountriesByPopulationData(**data_row)
            for data_row in dts[CountriesByPopulationData._table_position]
        ]

    @property
    def data(self) -> List[CountriesByPopulationData]:
        return deepcopy(self._data)
