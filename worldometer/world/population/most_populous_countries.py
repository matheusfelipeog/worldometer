from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple

from worldometer.scraper import get_data_tables


@dataclass
class CurrentMostPopulousCountriesData:
    position: int
    country: str
    population: int
    yearly_change: str
    world_share: str

    table_position = 0


@dataclass
class PastMostPopulousCountriesData:
    position: int
    country: str
    population: int
    world_share: str
    rank: str

    table_position = 1


@dataclass
class FutureMostPopulousCountriesData:
    position: int
    country: str
    population: int
    world_share: str
    rank: str

    table_position = 2


class MostPopulousCountries:

    source_path = '/population/most-populous-countries'
    new_column_names = (
        (
            'position',
            'country',
            'population',
            'yearly_change',
            'world_share'
        ),
        (
            'position',
            'country',
            'population',
            'world_share',
            'rank'
        ),
        (
            'position',
            'country',
            'population',
            'world_share',
            'rank'
        )
    )

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(
            self
    ) -> Tuple[
            List[CurrentMostPopulousCountriesData],
            List[PastMostPopulousCountriesData],
            List[FutureMostPopulousCountriesData]
    ]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                *self.new_column_names
            ]
        )

        return (
            [
                CurrentMostPopulousCountriesData(**data_row)
                for data_row in dts[CurrentMostPopulousCountriesData.table_position]
            ],
            [
                PastMostPopulousCountriesData(**data_row)
                for data_row in dts[PastMostPopulousCountriesData.table_position]
            ],
            [
                FutureMostPopulousCountriesData(**data_row)
                for data_row in dts[FutureMostPopulousCountriesData.table_position]
            ]
        )

    def current(self) -> List[CurrentMostPopulousCountriesData]:
        return deepcopy(self._data[0])

    def past(self) -> List[PastMostPopulousCountriesData]:
        return deepcopy(self._data[1])

    def future(self) -> List[FutureMostPopulousCountriesData]:
        return deepcopy(self._data[2])
