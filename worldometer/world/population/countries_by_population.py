from copy import deepcopy
from dataclasses import dataclass
from typing import List

from worldometer.scraper import get_data_tables


@dataclass
class CountriesByPopulationData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    idx: int
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
    """
    idx: int
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
    """Represents the data table of countries in the world by population.

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
    `Countries in the world by population <https://www.worldometers.info/world-population/population-by-country>`_.
    """
    source_path = '/world-population/population-by-country'
    new_column_names = (
        'idx',
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
        """Get a list of all the data from the table.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data)
