geography package
=================

.. contents:: Index
    :depth: 2

The `geography` package provides access to various data related to geographic information about the world, regions, and their countries.

To understand the significance of each of these data sets, their sources, and any other related information, please visit the official page at https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world


Countries in the world
----------------------

.. code-block::

    >>> from worldometer.world.geography import (
            WorldCountries,
            AsiaCountries,
            AfricaCountries,
            EuropeCountries,
            LatinAmericanAndTheCaribbeanCountries,
            NorthernAmericanCountries,
            OceaniaCountries
        )

    >>> wc = WorldCountries()

    >>> wc.total
    195

    >>> wc.countries()[0]
    WorldCountriesData(
        idx=1,
        country='India',
        population=1428627663,
        world_share='17.76 %',
        land_area=2973190
    )

    >>> ac = AfricaCountries()
    
    >>> ac.total
    54

    >>> ac.countries()[0]
    CountryData(
        idx=1,
        country='Nigeria',
        population=223804632,
        subregion='Western Africa'
    )

    >>> ac.dependencies()[0]
    DependencyData(
        idx=1,
        territory='Réunion',
        population=981796,
        dependency_of='France'
    )

.. module:: worldometer.world.geography.countries

.. autoclass:: WorldCountries
    :members:

.. autoclass:: AsiaCountries
    :members:
    :inherited-members:

.. autoclass:: AfricaCountries
    :members:
    :inherited-members:

.. autoclass:: EuropeCountries
    :members:
    :inherited-members:

.. autoclass:: LatinAmericanAndTheCaribbeanCountries
    :members:
    :inherited-members:

.. autoclass:: NorthernAmericanCountries
    :members:
    :inherited-members:

.. autoclass:: OceaniaCountries
    :members:
    :inherited-members:

.. autoclass:: WorldCountriesData
.. autoclass:: CountryData
.. autoclass:: DependencyData


Largest countries in the world
------------------------------

.. code-block::

    >>> from worldometer.world.geography import LargestCountries

    >>> lc = LargestCountries()

    >>> lc.data[0]
    LargestCountriesData(
        idx=1,
        country='Russia',
        total_area_km2=17098242,
        total_area_mi2=6601665,
        land_area_km2=16376870,
        land_area_mi2=6323142,
        percentage_of_world_landmass='11.0 %'
    )

.. module:: worldometer.world.geography.largest_countries

.. autoclass:: LargestCountries
    :members:

.. autoclass:: LargestCountriesData
