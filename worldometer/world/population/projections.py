from copy import deepcopy
from dataclasses import dataclass
from typing import List

from worldometer.scraper import get_data_tables


@dataclass
class WorldPopulationProjectionsData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    year: int
    world_population: int
    yearly_change: str
    net_change: int
    density: int
    """
    year: int
    world_population: int
    yearly_change: str
    net_change: int
    density: int

    _table_position = 0


class WorldPopulationProjections:
    """Represents the data table of the world population projections.

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
    `World Population Projections <https://www.worldometers.info/world-population/world-population-projections>`_.
    """
    source_path = '/world-population/world-population-projections'
    new_column_names = (
        'year',
        'world_population',
        'yearly_change',
        'net_change',
        'density'
    )

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(self) -> List[WorldPopulationProjectionsData]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                self.new_column_names
            ]
        )
        return [
            WorldPopulationProjectionsData(**data_row)
            for data_row in dts[WorldPopulationProjectionsData._table_position]
        ]

    @property
    def data(self) -> List[WorldPopulationProjectionsData]:
        """Get a list of all the data from the table.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data)
