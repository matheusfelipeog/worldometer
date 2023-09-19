from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple

from worldometer.scraper import get_data_tables


@dataclass
class CurrentWorldPopulationByRegionData:
    position: int
    region: str
    population: int
    yearly_change: str
    net_change: int
    density: int
    area: int
    migrants: int
    fertility_rate: float
    median_age: int
    urban_population: str
    world_share: str

    _table_position = 0


@dataclass
class PastWorldPopulationByRegionData:
    position: int
    region: str
    population: int
    world_share: str

    _table_position = 1


@dataclass
class FutureWorldPopulationByRegionData:
    position: int
    region: str
    population: int
    world_share: str

    _table_position = 2


class WorldPopulationByRegion:

    source_path = '/world-population/population-by-region'
    new_column_names = (
        (
            'position',
            'region',
            'population',
            'yearly_change',
            'net_change',
            'density',
            'area',
            'migrants',
            'fertility_rate',
            'median_age',
            'urban_population',
            'world_share'
        ),
        (
            'position',
            'region',
            'population',
            'world_share'
        ),
        (
            'position',
            'region',
            'population',
            'world_share'
        )
    )

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(
            self
    ) -> Tuple[
            List[CurrentWorldPopulationByRegionData],
            List[PastWorldPopulationByRegionData],
            List[FutureWorldPopulationByRegionData]
    ]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                *self.new_column_names
            ]
        )

        return (
            [
                CurrentWorldPopulationByRegionData(**data_row)
                for data_row in dts[CurrentWorldPopulationByRegionData._table_position]
            ],
            [
                PastWorldPopulationByRegionData(**data_row)
                for data_row in dts[PastWorldPopulationByRegionData._table_position]
            ],
            [
                FutureWorldPopulationByRegionData(**data_row)
                for data_row in dts[FutureWorldPopulationByRegionData._table_position]
            ]
        )

    def current(self) -> List[CurrentWorldPopulationByRegionData]:
        return deepcopy(self._data[0])

    def past(self) -> List[PastWorldPopulationByRegionData]:
        return deepcopy(self._data[1])

    def future(self) -> List[FutureWorldPopulationByRegionData]:
        return deepcopy(self._data[2])
