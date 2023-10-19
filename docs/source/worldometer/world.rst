world package
=============

.. module:: worldometer.world.counters

`world` is the main API of the `worldometer` package, where you can access various live counters and data available on the https://www.worldometers.info website through self-descriptive classes, methods, and attributes.


Live Counters
-------------

Get the data provided by the live counters.

Each section is represented by an attribute in the :class:`WorldCounters` class, and these attributes are instances of data classes that store the counter values.

Each of these data classes has attributes that describe the data stored in them.

.. code-block::

    >>> from worldometer.world import WorldCounters

    >>> wc = WorldCounters()

    >>> wc.world_population.current_population
    8065299074

    >>> wc.government_and_economics.computers_produced_this_year
    180248430

    >>> wc.society_and_media.internet_users_in_the_world_today
    5895566559

.. autoclass:: WorldCounters

.. autoclass:: WorldPopulation
.. autoclass:: GovernmentAndEconomics
.. autoclass:: SocietyAndMedia
.. autoclass:: Environment
.. autoclass:: Food
.. autoclass:: Water
.. autoclass:: Energy
.. autoclass:: Health


Country Codes
-------------

.. module:: worldometer.world.country_codes

All countries have specific codes that represent them in some way. Get all of these codes with the :class:`CountryCodes` class::
    
    >>> from worldometer.world import CountryCodes

    >>> cc = CountryCodes()

    >>> cc.data[0]
    CountryCodesData(
        country='Afghanistan',
        calling_code='93',
        three_letter_iso='AF',
        two_letter_iso='AFG',
        three_digit_iso_numeric=4
    )

.. autoclass:: CountryCodes
    :members:

.. autoclass:: CountryCodesData
