from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple

from worldometer.scraper import get_data_tables


@dataclass
class WorldCountriesData:
    idx: int
    country: str
    population: int
    world_share: str
    land_area: int

    _table_position = 0


@dataclass
class CountryData:
    idx: int
    country: str
    population: int
    subregion: str

    _table_position = 0


@dataclass
class DependencyData:
    idx: int
    territory: str
    population: int
    dependency_of: str

    _table_position = 1


class WorldCountries:

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
        return deepcopy(self._data[CountryData._table_position])  # type: ignore

    def dependencies(self) -> List[DependencyData]:
        return deepcopy(self._data[DependencyData._table_position])  # type: ignore


class AsiaCountries(_RegionCountries):
    source_path = '/geography/how-many-countries-in-asia'


class AfricaCountries(_RegionCountries):
    source_path = '/geography/how-many-countries-in-africa'


class EuropeCountries(_RegionCountries):
    source_path = '/geography/how-many-countries-in-europe'


class LatinAmericanAndTheCaribbeanCountries(_RegionCountries):
    source_path = '/geography/how-many-countries-in-latin-america'


class NorthernAmericanCountries(_RegionCountries):
    source_path = '/geography/how-many-countries-in-northern-america'


class OceaniaCountries(_RegionCountries):
    source_path = '/geography/how-many-countries-in-oceania'
