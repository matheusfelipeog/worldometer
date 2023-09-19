from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple

from worldometer.scraper import get_data_tables


@dataclass
class SubregionsData:
    area: int
    population: str

    _table_position = 0


@dataclass
class HistoricalData:
    year: int
    population: int
    yearly_change_percent: str
    yearly_change: int
    migrants: int
    median_age: float
    fertility_rate: float
    density: int
    urban_population_percent: str
    urban_population: int
    world_share: str
    world_population: int
    rank: int

    _table_position = 1


@dataclass
class ForecastData:
    year: int
    population: int
    yearly_change_percent: str
    yearly_change: int
    migrants: int
    median_age: float
    fertility_rate: float
    density: int
    urban_population_percent: str
    urban_population: int
    world_share: str
    world_population: int
    rank: int

    _table_position = 2


class AsiaPopulation:

    source_path = '/world-population/asia-population'
    new_column_names = (
        (
            'area',
            'population'
        ),
        (
            'year',
            'population',
            'yearly_change_percent',
            'yearly_change',
            'migrants',
            'median_age',
            'fertility_rate',
            'density',
            'urban_population_percent',
            'urban_population',
            'world_share',
            'world_population',
            'rank'
        ),
        (
            'year',
            'population',
            'yearly_change_percent',
            'yearly_change',
            'migrants',
            'median_age',
            'fertility_rate',
            'density',
            'urban_population_percent',
            'urban_population',
            'world_share',
            'world_population',
            'rank'
        )
    )

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(
            self
    ) -> Tuple[
            List[SubregionsData],
            List[HistoricalData],
            List[ForecastData]
    ]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                *self.new_column_names
            ]
        )

        return (
            [
                SubregionsData(**data_row)
                for data_row in dts[SubregionsData._table_position]
            ],
            [
                HistoricalData(**data_row)
                for data_row in dts[HistoricalData._table_position]
            ],
            [
                ForecastData(**data_row)
                for data_row in dts[ForecastData._table_position]
            ]
        )

    def subregions(self) -> List[SubregionsData]:
        return deepcopy(self._data[0])

    def historical(self) -> List[HistoricalData]:
        return deepcopy(self._data[1])

    def forecast(self) -> List[ForecastData]:
        return deepcopy(self._data[2])
