from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple, Union

from worldometer.scraper import get_data_tables, get_rts_counters_object


@dataclass
class SubregionData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    area: int
    population: str
    """
    area: int
    population: str

    _table_position = 0


@dataclass
class HistoricalData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    year: int
    population: int
    yearly_change_percent: str
    yearly_change: int
    migrants: int
    median_age: float
    fertility_rate: float
    density: int
    urban_population_percent: str
    urban_population: int
    world_share: str
    world_population: int
    rank: int
    """
    year: int
    population: int
    yearly_change_percent: str
    yearly_change: int
    migrants: int
    median_age: float
    fertility_rate: float
    density: int
    urban_population_percent: str
    urban_population: int
    world_share: str
    world_population: int
    rank: int

    _table_position = 1


@dataclass
class ForecastData:
    """Represents a data row from the respective table.

    Attributes
    ----------
    year: int
    population: int
    yearly_change_percent: str
    yearly_change: int
    migrants: int
    median_age: float
    fertility_rate: float
    density: int
    urban_population_percent: str
    urban_population: int
    world_share: str
    world_population: int
    rank: int
    """
    year: int
    population: int
    yearly_change_percent: str
    yearly_change: int
    migrants: int
    median_age: float
    fertility_rate: float
    density: int
    urban_population_percent: str
    urban_population: int
    world_share: str
    world_population: int
    rank: int

    _table_position = 2


class _RegionPopulation:

    _key_rts_counters = '[override]'
    source_path = '[override]'
    new_column_names = (
        (
            'area',
            'population'
        ),
        (
            'year',
            'population',
            'yearly_change_percent',
            'yearly_change',
            'migrants',
            'median_age',
            'fertility_rate',
            'density',
            'urban_population_percent',
            'urban_population',
            'world_share',
            'world_population',
            'rank'
        ),
        (
            'year',
            'population',
            'yearly_change_percent',
            'yearly_change',
            'migrants',
            'median_age',
            'fertility_rate',
            'density',
            'urban_population_percent',
            'urban_population',
            'world_share',
            'world_population',
            'rank'
        )
    )

    def __init__(self) -> None:
        self._data = self._load_data()

    def _load_data(
            self
    ) -> Tuple[
            List[SubregionData],
            List[HistoricalData],
            List[ForecastData]
    ]:
        dts = get_data_tables(
            path_url=self.source_path,
            new_column_names=[
                *self.new_column_names
            ]
        )

        return (
            [
                SubregionData(**data_row)
                for data_row in dts[SubregionData._table_position]
            ],
            [
                HistoricalData(**data_row)
                for data_row in dts[HistoricalData._table_position]
            ],
            [
                ForecastData(**data_row)
                for data_row in dts[ForecastData._table_position]
            ]
        )

    def live(self) -> Union[int, float, None]:
        """Get a live population counter for the respective region."""
        rts_counters = get_rts_counters_object(path_url=self.source_path)
        return rts_counters.get(self._key_rts_counters)

    def subregions(self) -> List[SubregionData]:
        """Get a list of all the subregions' data from the table.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data[SubregionData._table_position])  # type: ignore

    def historical(self) -> List[HistoricalData]:
        """Get a list of all historical data from the table.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data[HistoricalData._table_position])  # type: ignore

    def forecast(self) -> List[ForecastData]:
        """Get a list of all forecast data from the table.

        Each index in the list contains an object representing
        a data row of the table.
        """
        return deepcopy(self._data[ForecastData._table_position])  # type: ignore


class AsiaPopulation(_RegionPopulation):
    """Represents the data tables of Asia's populations.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original tables.

    Notes
    -----
    Check the source tables in
    `Asia Population <https://www.worldometers.info/world-population/asia-population>`_.
    """
    _key_rts_counters = 'asia-population'
    source_path = '/world-population/asia-population'


class AfricaPopulation(_RegionPopulation):
    """Represents the data tables of Africa's populations.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original tables.

    Notes
    -----
    Check the source tables in
    `Africa Population <https://www.worldometers.info/world-population/africa-population>`_.
    """
    _key_rts_counters = 'africa-population'
    source_path = '/world-population/africa-population'


class EuropePopulation(_RegionPopulation):
    """Represents the data tables of Europe's populations.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original tables.

    Notes
    -----
    Check the source tables in
    `Europe Population <https://www.worldometers.info/world-population/europe-population>`_.
    """
    _key_rts_counters = 'europe-population'
    source_path = '/world-population/europe-population'


class LatinAmericanAndTheCaribbeanPopulation(_RegionPopulation):
    """Represents the data tables of Latin American and Caribbean populations.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original tables.

    Notes
    -----
    Check the source tables in
    `Latin America and the Caribbean
    Population <https://www.worldometers.info/world-population/latin-america-and-the-caribbean-population'>`_.
    """
    _key_rts_counters = 'latin-america-and-the-caribbean-population'
    source_path = '/world-population/latin-america-and-the-caribbean-population'


class NorthernAmericanPopulation(_RegionPopulation):
    """Represents the data tables of Northern American populations.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original tables.

    Notes
    -----
    Check the source tables in
    `Northern American Population <https://www.worldometers.info/world-population/northern-america-population>`_.
    """
    _key_rts_counters = 'northern-america-population'
    source_path = '/world-population/northern-america-population'


class OceaniaPopulation(_RegionPopulation):
    """Represents the data tables of the Oceania populations.

    Attributes
    ----------
    source_path : str
        The data source path.
    new_column_names : tuple
        The new column names that will be used to replace those
        of the original tables.

    Notes
    -----
    Check the source tables in
    `Oceania Population <https://www.worldometers.info/world-population/oceania-population>`_.
    """
    _key_rts_counters = 'oceania-population'
    source_path = '/world-population/oceania-population'
