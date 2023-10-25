from copy import deepcopy
from dataclasses import dataclass
from typing import List

from worldometer.scraper import get_data_tables


@dataclass
class LargestCitiesData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    rank: int
    urban_area: str
    population_estimate: str
    country: str
    land_area: int
    density: int
    """
    rank: int
    urban_area: str
    population_estimate: str
    country: str
    land_area: int
    density: int

    _table_position = 0


class LargestCities:
    """Represents the data table of the largest cities in the world.

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
    `largest cities in the world <https://www.worldometers.info/population/largest-cities-in-the-world>`_.
    """
    source_path = '/population/largest-cities-in-the-world'
    new_column_names = (
        'rank',
        'urban_area',
        'population_estimate',
        'country',
        'land_area',
        'density'
    )

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(self) -> List[LargestCitiesData]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                self.new_column_names
            ],
            attrs=None
        )
        return [
            LargestCitiesData(**data_row)
            for data_row in dts[LargestCitiesData._table_position]
        ]

    @property
    def data(self) -> List[LargestCitiesData]:
        """Get a list of all the data from the table.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data)
