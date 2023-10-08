"""
geography package
-----------------

The `geography` package provides access to various data related
to geographic information about the world, regions, and their countries.

To understand the significance of each of these data sets,
their sources, and any other related information,
please visit the official page at https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world
"""

__all__ = [
    'LargestCountries',
    'WorldCountries',
    'AsiaCountries',
    'AfricaCountries',
    'EuropeCountries',
    'LatinAmericanAndTheCaribbeanCountries',
    'NorthernAmericanCountries',
    'OceaniaCountries'
]

from worldometer.world.geography.largest_countries import LargestCountries
from worldometer.world.geography.countries import (
    WorldCountries,
    AsiaCountries,
    AfricaCountries,
    EuropeCountries,
    LatinAmericanAndTheCaribbeanCountries,
    NorthernAmericanCountries,
    OceaniaCountries
)
