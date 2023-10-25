from copy import deepcopy
from dataclasses import dataclass
from typing import List

from worldometer.scraper import get_data_tables


@dataclass
class LargestCountriesData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    idx: int
    country: str
    total_area_km2: int
    total_area_mi2: int
    land_area_km2: int
    land_area_mi2: int
    percentage_of_world_landmass: str
    """
    idx: int
    country: str
    total_area_km2: int
    total_area_mi2: int
    land_area_km2: int
    land_area_mi2: int
    percentage_of_world_landmass: str

    _table_position = 0


class LargestCountries:
    """Represents the data table of the largest countries in the world (by area).

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
    `Largest Countries in the World <https://www.worldometers.info/geography/largest-countries-in-the-world>`_.
    """
    source_path = '/geography/largest-countries-in-the-world'
    new_column_names = (
        'idx',
        'country',
        'total_area_km2',
        'total_area_mi2',
        'land_area_km2',
        'land_area_mi2',
        'percentage_of_world_landmass'
    )

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(self) -> List[LargestCountriesData]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                self.new_column_names
            ]
        )
        return [
            LargestCountriesData(**data_row)
            for data_row in dts[LargestCountriesData._table_position]
        ]

    @property
    def data(self) -> List[LargestCountriesData]:
        """Get a list of all the data from the table.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data)
