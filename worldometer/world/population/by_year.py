from copy import deepcopy
from dataclasses import dataclass
from typing import List

from worldometer.scraper import get_data_tables


@dataclass
class WorldPopulationByYearData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    year: int
    world_population: int
    yearly_change: str
    net_change: float
    density: float
    """
    year: int
    world_population: int
    yearly_change: str
    net_change: float
    density: float

    _table_position = 0


class WorldPopulationByYear:
    """Represents the data table of the world population by year.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original table.

    Notes
    -----
    Check the source table in the
    `world population by year <https://www.worldometers.info/world-population/world-population-by-year>`_.
    """
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
        """Get a list of all the data from the table.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data)
