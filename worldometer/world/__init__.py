"""
world package
-------------

`world` is the main API of the `worldometer` package,
where you can access various live counters and data
available on the https://www.worldometers.info website
through self-descriptive classes, methods, and attributes.
"""

__all__ = [
    'geography',
    'population',
    'CountryCodes',
    'WorldCounters'
]

from worldometer.world import geography
from worldometer.world import population
from worldometer.world.country_codes import CountryCodes
from worldometer.world.counters import WorldCounters
