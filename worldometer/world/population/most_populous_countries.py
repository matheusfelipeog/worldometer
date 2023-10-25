from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple

from worldometer.scraper import get_data_tables


@dataclass
class CurrentMostPopulousCountriesData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    idx: int
    country: str
    population: int
    yearly_change: str
    world_share: str
    """
    idx: int
    country: str
    population: int
    yearly_change: str
    world_share: str

    _table_position = 0


@dataclass
class PastMostPopulousCountriesData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    idx: int
    country: str
    population: int
    world_share: str
    rank: str
    """
    idx: int
    country: str
    population: int
    world_share: str
    rank: str

    _table_position = 1


@dataclass
class FutureMostPopulousCountriesData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    idx: int
    country: str
    population: int
    world_share: str
    rank: str
    """
    idx: int
    country: str
    population: int
    world_share: str
    rank: str

    _table_position = 2


class MostPopulousCountries:
    """Represents the data table of most populous countries in the world.

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
    `Most populous countries in the world <https://www.worldometers.info/population/most-populous-countries>`_.
    """
    source_path = '/population/most-populous-countries'
    new_column_names = (
        (
            'idx',
            'country',
            'population',
            'yearly_change',
            'world_share'
        ),
        (
            'idx',
            'country',
            'population',
            'world_share',
            'rank'
        ),
        (
            'idx',
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
                for data_row in dts[CurrentMostPopulousCountriesData._table_position]
            ],
            [
                PastMostPopulousCountriesData(**data_row)
                for data_row in dts[PastMostPopulousCountriesData._table_position]
            ],
            [
                FutureMostPopulousCountriesData(**data_row)
                for data_row in dts[FutureMostPopulousCountriesData._table_position]
            ]
        )

    def current(self) -> List[CurrentMostPopulousCountriesData]:
        """Get a list of all the current data from the table.

        These data are related to the current year.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data[CurrentMostPopulousCountriesData._table_position])  # type: ignore

    def past(self) -> List[PastMostPopulousCountriesData]:
        """Get a list of all historical data from the table.

        These data pertain to the year 1950.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data[PastMostPopulousCountriesData._table_position])  # type: ignore

    def future(self) -> List[FutureMostPopulousCountriesData]:
        """Get a list of all future data from the table.

        These data are an estimate for the year 2050.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data[FutureMostPopulousCountriesData._table_position])  # type: ignore
