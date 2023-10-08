"""
worldometer package
-------------------

The `worldometer` package accesses various counters and live data available
throughout the https://www.worldometers.info website and provides them
through self-describing classes, methods and attributes.

Examples
--------
Get the data from the live counters available on the homepage:

>>> from worldometer.world import WorldCounters

>>> wc = WorldCounters()

>>> wc.world_population.current_population
8065299074

>>> wc.government_and_economics.computers_produced_this_year
180248430

>>> wc.society_and_media.internet_users_in_the_world_today
5895566559

Reload data to get the latest:

>>> wc.reload_data()
>>> wc.world_population.current_population
8065300592

Get help and view information about mapped sections:

>>> help(wc)

Notes
-----
Check https://www.worldometers.info/about for more information about
the data source, how live counters work, and more related information.
"""

__all__ = [
    'core',
    'api'
]

from .__about__ import __version__, __author__, __email__

from .core import Worldometer
from .api import *
