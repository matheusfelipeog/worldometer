.. worldometer documentation master file, created by
   sphinx-quickstart on Mon Feb 15 22:32:37 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Worldometer: Scraping & API
===========================

.. image:: https://img.shields.io/pypi/status/worldometer?style=for-the-badge
    :alt: PyPI - Status
    :target: https://pypi.org/project/worldometer/

.. image:: https://img.shields.io/pypi/v/worldometer?style=for-the-badge
    :alt: PyPI
    :target: https://pypi.org/project/worldometer/

.. image:: https://img.shields.io/github/v/release/matheusfelipeog/worldometer?style=for-the-badge
    :alt: GitHub release (latest by date)
    :target: https://github.com/matheusfelipeog/worldometer/releases

.. image:: https://img.shields.io/github/license/matheusfelipeog/worldometer?style=for-the-badge
    :alt: License MIT
    :target: https://github.com/matheusfelipeog/worldometer/blob/master/LICENSE

Get current metrics in the world with the python **worldometer** module

-----------------------------------------------------------------------


Index
-----

- `About <#id1>`_

  - `worldometers <#id2>`_
  - `How it works? <#id3>`_

- `Install <#id4>`_
- `Demo <#id5>`_
- `Contributions <#id6>`_
- `License <#id7>`_
- `Indices and tables <#id8>`_

**Worldometer Docs:**

.. toctree::
    :maxdepth: 1

    worldometer_core
    worldometer_api


About
-----

`Worldometer <https://github.com/matheusfelipeog/worldometer>`_ is a python module that collects data from `worldometers.info <https://www.worldometers.info/>`_ and provides a simple and self-explanatory interface for using the data.

worldometers.info
^^^^^^^^^^^^^^^^^

    "Worldometer is run by an international team of developers, researchers, and volunteers with the goal of making world statistics available in a thought-provoking and time relevant format to a wide audience around the world. It is published by a small and independent digital media company based in the United States. We have no political, governmental, or corporate affiliation. Furthermore, we have no investors, donors, grants, or backers of any type. We are completely independent and self-financed through automated programmatic advertising sold in real time on multiple ad exchanges."

More info: `worldometers.info/about <https://www.worldometers.info/about/>`_

How it works?
^^^^^^^^^^^^^

    **[Adapted]:** "For the data, is elaborate instead a real-time estimate through a proprietary algorithm which processes the latest data and projections provided by the most reputable organizations and statistical offices in the world."

More info about data source: `worldometers.info/sources <https://www.worldometers.info/sources/>`_


Install
-------

First, create a directory and enter it::

    $ mkdir my_project && cd my_project

Create a virtual environment to avoid breaking dependence on other projects.

This project uses `pipenv <https://pipenv.pypa.io/en/latest/>`_, it already does it alone 😆::

    $ pipenv install worldometer


But you can use ``virtualenv`` + ``pip`` if you prefer::

    $ virtualenv venv && source venv/Scripts/activate


Now install::

    $ pip install worldometer


Demo
----

.. note:: 
    The first time you run any function/method or class, it will download Chromium to its home directory (for example, ``~/.pyppeteer/``). It only happens once.

    After, it will only open the chromium to render the contents of worldometers.

**Simple API usage:**

*See all function in:* `worldometer.api <worldometer_api.html>`_

Get metrics using simplified functions:

    >>> import worldometer

    >>> worldometer.current_world_population()
    {'current_world_population': 7845085923}

    >>> worldometer.tweets_sent_today()
    {'tweets_sent_today': 4539558}

Get metrics by passing the corresponding label:

    >>> worldometer.get_metric_of(label='computers_produced_this_year')
    {'computers_produced_this_year': 27760858}


**Or complete use with Worldometer Class:**

*See all methods in:* `worldometer.core <worldometer_core.html>`_

>>> from worldometer import Worldometer
>>> w = Worldometer()

Get the number of categories, labels and metrics in ``w`` object:

    >>> w.what_is_here()
    {'categories': 8, 'labels': 63, 'metrics': 63}

Get all categories used:

    >>> w.categories()
    [   
        'world_population',
        'government_and_economics',
        'society_and_media',
        ...  # compressed
    ]

Get all labels used:

    >>> w.metrics_labels()
    [   
        'current_world_population',
        'births_this_year',
        'births_today',
        'deaths_this_year',
        'deaths_today',
        'net_population_growth_this_year',
        ...  # compressed
    ]

Get all metrics used:

    >>> w.metrics()
    [   
        7845087963,
        15741371,
        5676,
        6608605,
        2383,
        9132766,
        ...  # compressed
    ]

Get all metrics with labels in dict format:

>>> w.metrics_with_labels()
{   
    'abortions_this_year': 4785492,
    'bicycles_produced_this_year': 17070566,
    'births_this_year': 15741371,
    'births_today': 5676,
    'blog_posts_written_today': 110171,
    'cars_produced_this_year': 8999185,
    'cellular_phones_sold_today': 98846,
    ...: ...  # compressed
}


Contributions
-------------

All contributions are welcome!

Found a problem, want to give a tip? `open an issue <https://github.com/matheusfelipeog/worldometer/issues>`_

Do you have a solution to the problem? `Send me a PR <https://github.com/matheusfelipeog/worldometer/pulls>`_

Did you like this project? `Click on the star ⭐ <https://github.com/matheusfelipeog/worldometer/stargazers>`_


License
-------

This project is using the MIT license, see in `MIT LICENSE <https://github.com/matheusfelipeog/worldometer/blob/master/LICENSE>`_


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
