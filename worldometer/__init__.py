# -*- coding: utf-8 -*-

"""
Worldometer Module
------------------

Get metrics from around the world in multiple categories.

Examples
--------
You can use the simplified API to collect the data:

>>> import worldometer

>>> worldometer.current_world_population()
{'current_world_population': 7845085923}

>>> worldometer.tweets_sent_today()
{'tweets_sent_today': 4539558}

>>> worldometer.get_metric_of(label='computers_produced_this_year')
{'computers_produced_this_year': 27760858}

Or using Worldometer Class:

>>> from worldometer import Worldometer
>>> w = Worldometer()

>>> w.what_is_here()
{'categories': 8, 'labels': 63, 'metrics': 63}

>>> w.categories()
[   
    'world_population',
    'government_and_economics',
    'society_and_media',
    ...
]

>>> w.metrics_labels()
[   
    'current_world_population',
    'births_this_year',
    'births_today',
    'deaths_this_year',
    'deaths_today',
    'net_population_growth_this_year',
    ...
]

>>> w.metrics()
[   
    7845087963,
    15741371,
    5676,
    6608605,
    2383,
    9132766,
    ...
]

>>> w.metrics_with_labels()
{   
    'abortions_this_year': 4785492,
    'bicycles_produced_this_year': 17070566,
    'births_this_year': 15741371,
    'births_today': 5676,
    'blog_posts_written_today': 110171,
    'cars_produced_this_year': 8999185,
    'cellular_phones_sold_today': 98846,
    ...: ...
}

More info: github.com/matheusfelipeog/worldometer
"""


__all__ = [
    'core',
    'api'
]

from .__about__ import __version__, __author__, __email__

from .core import Worldometer
from .api import *
