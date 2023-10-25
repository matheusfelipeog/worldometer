from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple

from worldometer.scraper import get_data_tables


@dataclass
class WorldCountriesData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    idx: int
    country: str
    population: int
    world_share: str
    land_area: int
    """
    idx: int
    country: str
    population: int
    world_share: str
    land_area: int

    _table_position = 0


@dataclass
class CountryData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    idx: int
    country: str
    population: int
    subregion: str
    """
    idx: int
    country: str
    population: int
    subregion: str

    _table_position = 0


@dataclass
class DependencyData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    idx: int
    territory: str
    population: int
    dependency_of: str
    """
    idx: int
    territory: str
    population: int
    dependency_of: str

    _table_position = 1


class WorldCountries:
    """Represents the data table of a list of countries in the world.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original table.
    total : int
        The total number of countries in the world.


    Notes
    -----
    Check the source table in
    `List of countries <https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world>`_.
    """
    source_path = '/geography/how-many-countries-are-there-in-the-world'
    new_column_names = (
        'idx',
        'country',
        'population',
        'world_share',
        'land_area'
    )

    def __init__(self) -> None:
        self._data = self._load_data()
        self.total = len(self._data)

    def _load_data(self) -> List[WorldCountriesData]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                self.new_column_names
            ]
        )
        return [
            WorldCountriesData(**data_row)
            for data_row in dts[WorldCountriesData._table_position]
        ]

    def countries(self) -> List[WorldCountriesData]:
        """Get a list of all the countries' data from the table.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data)


class _RegionCountries:

    source_path = '[override]'
    new_column_names = (
        (
            'idx',
            'country',
            'population',
            'subregion'
        ),
        (
            'idx',
            'territory',
            'population',
            'dependency_of'
        )
    )

    def __init__(self) -> None:
        self._data = self._load_data()
        self.total = len(self._data[CountryData._table_position])

    def _load_data(
            self
    ) -> Tuple[
            List[CountryData],
            List[DependencyData]
    ]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                *self.new_column_names
            ]
        )

        return (
            [
                CountryData(**data_row)
                for data_row in dts[CountryData._table_position]
            ],
            [
                DependencyData(**data_row)
                for data_row in dts[DependencyData._table_position]
            ]
        )

    def countries(self) -> List[CountryData]:
        """Get a list of all the data for countries in the
        region from the table.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data[CountryData._table_position])  # type: ignore

    def dependencies(self) -> List[DependencyData]:
        """Get a list of all the data for dependencies in the
        region from the table.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data[DependencyData._table_position])  # type: ignore


class AsiaCountries(_RegionCountries):
    """Represents the data tables of Asia's countries.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original tables.
    total : int
        The total number of countries in the region.

    Notes
    -----
    Check the source tables in
    `Countries in Asia <https://www.worldometers.info/geography/how-many-countries-in-asia>`_.
    """
    source_path = '/geography/how-many-countries-in-asia'


class AfricaCountries(_RegionCountries):
    """Represents the data tables of Africa's countries.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original tables.
    total : int
        The total number of countries in the region.

    Notes
    -----
    Check the source tables in
    `Countries in Africa <https://www.worldometers.info/geography/how-many-countries-in-africa>`_.
    """
    source_path = '/geography/how-many-countries-in-africa'


class EuropeCountries(_RegionCountries):
    """Represents the data tables of Europe's countries.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original tables.
    total : int
        The total number of countries in the region.

    Notes
    -----
    Check the source tables in
    `Countries in Europe <https://www.worldometers.info/geography/how-many-countries-in-europe>`_.
    """
    source_path = '/geography/how-many-countries-in-europe'


class LatinAmericanAndTheCaribbeanCountries(_RegionCountries):
    """Represents the data tables of Latin American And The Caribbean countries.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original tables.
    total : int
        The total number of countries in the region.

    Notes
    -----
    Check the source tables in
    `Countries in Latin American And The
    Caribbean <https://www.worldometers.info/geography/how-many-countries-in-latin-america>`_.
    """
    source_path = '/geography/how-many-countries-in-latin-america'


class NorthernAmericanCountries(_RegionCountries):
    """Represents the data tables of Northern American countries.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original tables.
    total : int
        The total number of countries in the region.

    Notes
    -----
    Check the source tables in
    `Countries in Northern American <https://www.worldometers.info/geography/how-many-countries-in-northern-america>`_.
    """
    source_path = '/geography/how-many-countries-in-northern-america'


class OceaniaCountries(_RegionCountries):
    """Represents the data tables of the Oceania countries.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original tables.
    total : int
        The total number of countries in the region.

    Notes
    -----
    Check the source tables in
    `Countries in Oceania <https://www.worldometers.info/geography/how-many-countries-in-oceania>`_.
    """
    source_path = '/geography/how-many-countries-in-oceania'
