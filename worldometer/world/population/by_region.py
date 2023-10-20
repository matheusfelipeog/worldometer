from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple

from worldometer.scraper import get_data_tables


@dataclass
class CurrentWorldPopulationByRegionData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    idx: int
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
    """
    idx: int
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
    """Represents a data row from the respective table.

    Attributes
    ----------
    idx: int
    region: str
    population: int
    world_share: str
    """
    idx: int
    region: str
    population: int
    world_share: str

    _table_position = 1


@dataclass
class FutureWorldPopulationByRegionData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    idx: int
    region: str
    population: int
    world_share: str
    """
    idx: int
    region: str
    population: int
    world_share: str

    _table_position = 2


class WorldPopulationByRegion:
    """Represents the data table of regions in the world by population.

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
    `Regions in the world by population <https://www.worldometers.info/world-population/population-by-region>`_.
    """
    source_path = '/world-population/population-by-region'
    new_column_names = (
        (
            'idx',
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
            'idx',
            'region',
            'population',
            'world_share'
        ),
        (
            'idx',
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
        """Get a list of all the current data from the table.

        These data are related to the current year.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data[CurrentWorldPopulationByRegionData._table_position])  # type: ignore

    def past(self) -> List[PastWorldPopulationByRegionData]:
        """Get a list of all historical data from the table.

        These data pertain to the year 1950.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data[PastWorldPopulationByRegionData._table_position])  # type: ignore

    def future(self) -> List[FutureWorldPopulationByRegionData]:
        """Get a list of all future data from the table.

        These data are an estimate for the year 2050.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data[FutureWorldPopulationByRegionData._table_position])  # type: ignore
