from copy import deepcopy
from dataclasses import dataclass
from typing import List

from worldometer.scraper import get_data_tables


@dataclass
class WorldPopulationByYearData:
    year: int
    world_population: int
    yearly_change: str
    net_change: float
    density: float

    _table_position = 0


class WorldPopulationByYear:

    source_path = '/world-population/world-population-by-year'
    new_column_names = (
        'year',
        'world_population',
        'yearly_change',
        'net_change',
        'density'
    )

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(self) -> List[WorldPopulationByYearData]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                self.new_column_names
            ]
        )
        return [
            WorldPopulationByYearData(**data_row)
            for data_row in dts[WorldPopulationByYearData._table_position]
        ]

    @property
    def data(self) -> List[WorldPopulationByYearData]:
        return deepcopy(self._data)
