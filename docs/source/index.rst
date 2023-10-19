.. worldometer documentation master file, created by
   sphinx-quickstart on Mon Feb 15 22:32:37 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. this title is hidden with css

Worldometer
===========

.. image:: https://raw.githubusercontent.com/matheusfelipeog/worldometer/master/.github/assets/images/worldometer.png
    :alt: Worldometer package logo
    :width: 800px
    :align: center
    
*Get live, population, geography, projected, and historical data from around the world.*

.. image:: https://img.shields.io/pypi/v/worldometer
    :alt: PyPI - Version
    :target: https://pypi.org/project/worldometer/

.. image:: https://pepy.tech/badge/worldometer
    :alt: Total Downloads
    :target: https://pepy.tech/project/worldometer

.. image:: https://img.shields.io/github/license/matheusfelipeog/worldometer
    :alt: License MIT
    :target: https://github.com/matheusfelipeog/worldometer/blob/master/LICENSE

.. image:: https://img.shields.io/pypi/status/worldometer
    :alt: PyPI - Status
    :target: https://pypi.org/project/worldometer/

.. image:: https://readthedocs.org/projects/worldometer/badge/?version=latest
    :alt: Documentation Status
    :target: https://worldometer.readthedocs.io/en/latest/?badge=latest


-----------------------------------------------------------------------


About
-----

The `worldometer <https://github.com/matheusfelipeog/worldometer>`_ package accesses various counters and live data available throughout the `worldometers.info <https://www.worldometers.info/>`_ website and provides them through simple and self-describing classes, methods and attributes.

Access data on:

- The world 🌍
- Population 👥
- Geography 🗺️
- Projections 🔮
- Historical 📜


Install
-------

Use ``pip`` to install the worldometer package::

    $ pip install worldometer


API Reference
-------------

The worldometer package is divided into several specific sub-packages for each dataset. So if you are looking for information on a specific package, class, or method, this part of the documentation is for you.

.. toctree::
    :maxdepth: 2

    worldometer <worldometer/index>
    worldometer.world <worldometer/world>
    worldometer.world.population <worldometer/population>
    worldometer.world.geography <worldometer/geography>


Demo
----

.. note:: 
    The first time you run any function/method or class, it will download Chromium to ``~/.local/share/pyppeteer`` directory. It only happens once. After, it will only open the chromium to render the contents of worldometers.info.

Get the data from the live counters available on the `homepage <https://www.worldometers.info/>`_::

    >>> from worldometer.world import WorldCounters

    >>> wc = WorldCounters()

    >>> wc.world_population.current_population
    8065299074

    >>> wc.government_and_economics.computers_produced_this_year
    180248430

    >>> wc.society_and_media.internet_users_in_the_world_today
    5895566559

Reload data to get the latest::

    >>> wc.reload_data()
    >>> wc.world_population.current_population
    8065300592

Get help and view information about mapped sections::

    >>> help(wc)


worldometers.info
-----------------

    "Worldometer is run by an international team of developers, researchers, and volunteers with the goal of making world statistics available in a thought-provoking and time relevant format to a wide audience around the world. It is published by a small and independent digital media company based in the United States. We have no political, governmental, or corporate affiliation. Furthermore, we have no investors, donors, grants, or backers of any type. We are completely independent and self-financed through automated programmatic advertising sold in real time on multiple ad exchanges."

More info: `worldometers.info/about <https://www.worldometers.info/about/>`_


Data Sources
------------

    **[adapted]:** "worldometers.info collects its statistics and data from the most reputable national and international organizations, including the United Nations, the World Health Organization, the Food and Agriculture Organization, OECD and others.

    Each Worldometer counter has its specific set of sources, which are listed on its dedicated page (accessible by clicking on the counter text link, when available).

    Data, estimates, and projections displayed on worldometers.info counters are for the most part provided by organizations included in the following list of United Nations Statistics Division's partners."

More info about data source: `worldometers.info/sources <https://www.worldometers.info/sources/>`_


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
