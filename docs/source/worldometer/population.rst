population package
==================

.. contents:: Index
    :depth: 2

The population package provides access to various data related to world populations, regions, and their countries. Additionally, it includes historical data ranging from 1950 to the present day and future projections extending to 2050.

To understand the significance of each of these data sets, their sources, and any other related information, please visit the official page at https://www.worldometers.info/population


Population by country
---------------------

.. code-block::

    >>> from worldometer.world.population import CountriesByPopulation

    >>> cp = CountriesByPopulation()

    >>> cp.data[0]
    CountriesByPopulationData(
        idx=1,
        country='India',
        population=1428627663,
        yearly_change='0.81 %',
        net_change=11454490,
        density=481,
        land_area=2973190,
        migrants=-486136,
        fertility_rate=2.0,
        median_age=28.0,
        urban_population='36 %',
        world_share='17.76 %'
    )

.. module:: worldometer.world.population.countries_by_population

.. autoclass:: CountriesByPopulation
    :members:

.. autoclass:: CountriesByPopulationData


Population by region
--------------------

.. code-block::

    >>> from worldometer.world.population import WorldPopulationByRegion

    >>> pr = WorldPopulationByRegion()

    >>> pr.current()[0]
    CurrentWorldPopulationByRegionData(
        idx=1,
        region='Asia',
        population=4753079727,
        yearly_change='0.64 %',
        net_change=30444963,
        density=153,
        area=31033131,
        migrants=-1487191,
        fertility_rate=1.934,
        median_age=32,
        urban_population='52.6 %',
        world_share='59.1 %'
    )

    >>> pr.past()[0]
    PastWorldPopulationByRegionData(
        idx=1,
        region='Asia',
        population=1379048370,
        world_share='55.2 %'
    )

    >>> pr.future()[0]
    FutureWorldPopulationByRegionData(
        idx=1,
        region='Asia',
        population=5292947571,
        world_share='54.5 %'
    )

.. module:: worldometer.world.population.by_region

.. autoclass:: WorldPopulationByRegion
    :members:

.. autoclass:: CurrentWorldPopulationByRegionData
.. autoclass:: PastWorldPopulationByRegionData
.. autoclass:: FutureWorldPopulationByRegionData


Population by year
------------------

.. code-block::

    >>> from worldometer.world.population import WorldPopulationByYear

    >>> py = WorldPopulationByYear()

    >>> py.data[0]
    WorldPopulationByYearData(
        year=2023,
        world_population=8045311447,
        yearly_change='0.88 %',
        net_change=70206291.0,
        density=54.0
    )

.. module:: worldometer.world.population.by_year

.. autoclass:: WorldPopulationByYear
    :members:

.. autoclass:: WorldPopulationByYearData


Largest cities in the world
---------------------------

.. code-block::

    >>> from worldometer.world.population import LargestCities

    >>> lc = LargestCities()

    >>> lc.data[0]
    LargestCitiesData(
        rank=1,
        urban_area='Tokyo-Yokohama',
        population_estimate=37843000,
        country='Japan',
        land_area=8547,
        density=4400
    )

.. module:: worldometer.world.population.largest_cities

.. autoclass:: LargestCities
    :members:

.. autoclass:: LargestCitiesData


Most populous countries
-----------------------

.. code-block::

    >>> from worldometer.world.population import MostPopulousCountries

    >>> pc = MostPopulousCountries()

    >>> pc.current()[0]
    CurrentMostPopulousCountriesData(
        idx=1,
        country='India',
        population=1428627663,
        yearly_change='0.81 %',
        world_share='17.8 %'
    )

    >>> pc.past()[0]
    PastMostPopulousCountriesData(
        idx=1,
        country='China',
        population=543979233,
        world_share='21.8 %',
        rank='(2)'
    )

    >>> pc.future()[0]
    FutureMostPopulousCountriesData(
        idx=1,
        country='India',
        population=1670490596,
        world_share='17.2 %',
        rank='(1)'
    )

.. module:: worldometer.world.population.most_populous_countries

.. autoclass:: MostPopulousCountries
    :members:

.. autoclass:: CurrentMostPopulousCountriesData
.. autoclass:: PastMostPopulousCountriesData
.. autoclass:: FutureMostPopulousCountriesData


World population projections
----------------------------

.. code-block::

    >>> from worldometer.world.population import WorldPopulationProjections

    >>> pp = WorldPopulationProjections()

    >>> pp.data[0]
    WorldPopulationProjectionsData(
        year=2023,
        world_population=8045311447,
        yearly_change='0.88 %',
        net_change=70206291,
        density=54
    )

.. module:: worldometer.world.population.projections

.. autoclass:: WorldPopulationProjections
    :members:

.. autoclass:: WorldPopulationProjectionsData


Regions population
------------------

.. code-block::

    >>> from worldometer.world.population import (
            AsiaPopulation,
            AfricaPopulation,
            EuropePopulation,
            LatinAmericanAndTheCaribbeanPopulation,
            NorthernAmericanPopulation,
            OceaniaPopulation
        )

    >>> ap = AsiaPopulation()

    >>> ap.live()
    4762699828

    >>> ap.subregions()[0]
    SubregionData(
        area='Southern Asia',
        population='(2,027,578,876)'
    )

    >>> ap.historical()[0]
    HistoricalData(
        year=2023,
        population=4753079727,
        yearly_change_percent='0.64 %',
        yearly_change=30444963,
        migrants=-1487191,
        median_age=31.9,
        fertility_rate=1.93,
        density=153,
        urban_population_percent='52.6 %',
        urban_population=2500201501,
        world_share='59.1 %',
        world_population=8045311447,
        rank=nan
    )

    >>> ap.forecast()[0]
    ForecastData(
        year=2025,
        population=4816249054,
        yearly_change_percent='0.64 %',
        yearly_change=30384996,
        migrants=-1555419,
        median_age=32.7,
        fertility_rate=1.93,
        density=155,
        urban_population_percent='53.8 %',
        urban_population=2589655469,
        world_share='61.4 %',
        world_population=8191988453,
        rank=nan
    )

.. module:: worldometer.world.population.regions

.. autoclass:: AsiaPopulation
    :members:
    :inherited-members:

.. autoclass:: AfricaPopulation
    :members:
    :inherited-members:

.. autoclass:: EuropePopulation
    :members:
    :inherited-members:

.. autoclass:: LatinAmericanAndTheCaribbeanPopulation
    :members:
    :inherited-members:

.. autoclass:: NorthernAmericanPopulation
    :members:
    :inherited-members:

.. autoclass:: OceaniaPopulation
    :members:
    :inherited-members:

.. autoclass:: SubregionData
.. autoclass:: HistoricalData
.. autoclass:: ForecastData
