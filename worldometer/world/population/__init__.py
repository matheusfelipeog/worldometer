"""
population package
------------------

The `population` package provides access to various data related
to world populations, regions, and their countries. Additionally,
it includes historical data ranging from 1950 to the present day
and future projections extending to 2050.

To understand the significance of each of these data sets,
their sources, and any other related information,
please visit the official page at https://www.worldometers.info/population
"""

__all__ = [
    'CountriesByPopulation',
    'LargestCities',
    'MostPopulousCountries',
    'WorldPopulationByRegion',
    'WorldPopulationByYear',
    'WorldPopulationProjections',
    'AsiaPopulation',
    'AfricaPopulation',
    'EuropePopulation',
    'LatinAmericanAndTheCaribbeanPopulation',
    'NorthernAmericanPopulation',
    'OceaniaPopulation'
]

from worldometer.world.population.countries_by_population import CountriesByPopulation
from worldometer.world.population.largest_cities import LargestCities
from worldometer.world.population.most_populous_countries import MostPopulousCountries
from worldometer.world.population.by_region import WorldPopulationByRegion
from worldometer.world.population.by_year import WorldPopulationByYear
from worldometer.world.population.projections import WorldPopulationProjections
from worldometer.world.population.regions import (
    AsiaPopulation,
    AfricaPopulation,
    EuropePopulation,
    LatinAmericanAndTheCaribbeanPopulation,
    NorthernAmericanPopulation,
    OceaniaPopulation
)
