<p align="center">
    <img src="https://raw.githubusercontent.com/matheusfelipeog/worldometer/master/.github/assets/images/worldometer.png" alt="Worldometer package logo" width="800px" />
    <br />
    <em>Get live, population, geography, projected, and historical data from around the world.</em>
</p>

---

<p align="center">
    <sup>Metadata</sup>
    <br />
    <a href="https://pypi.org/project/worldometer/">
        <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/worldometer" />
    </a>
    <a href="https://pepy.tech/project/worldometer">
        <img alt="Total Downloads" src="https://pepy.tech/badge/worldometer" />
    </a>
    <a href="https://github.com/matheusfelipeog/worldometer/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/matheusfelipeog/worldometer" alt="License MIT" />
    </a>
</p>

<p align="center">
    <sup>Status</sup>
    <br />
    <a href="https://pypi.org/project/worldometer/">
        <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/worldometer" />
    </a>
    <a href='https://worldometer.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/worldometer/badge/?version=latest' alt='Documentation Status' />
    </a>
</p>


## Index

- [About](#about)
- [Install](#install)
- [Documentation](#documentation)
- [Demo](#demo)
- [worldometers.info](#worldometersinfo)
- [Data Sources](#data-sources)
- [Contributions](#contributions)
- [License](#license)


## About

The [`worldometer`](https://github.com/matheusfelipeog/worldometer) package accesses various counters and live data available throughout the [worldometers.info](https://www.worldometers.info/) website and provides them through simple and self-describing classes, methods and attributes.

Access data on:

- The world 🌍
- Population 👥
- Geography 🗺️
- Projections 🔮
- Historical 📜


## Install

Use `pip` to install the worldometer package:

```bash
$ pip install worldometer
```


## Documentation

See the docs for more information and its API at: [worldometer.readthedocs.io](https://worldometer.readthedocs.io/)


## Demo

> [!NOTE]
> *The first time you run any function/method or class, it will download Chromium to  `~/.local/share/pyppeteer` directory. It only happens once. After, it will only open the chromium to render the contents of worldometers.info.*

Get the data from the live counters available on the [homepage](https://www.worldometers.info/):

```python
>>> from worldometer.world import WorldCounters

>>> wc = WorldCounters()

>>> wc.world_population.current_population
8065299074

>>> wc.government_and_economics.computers_produced_this_year
180248430

>>> wc.society_and_media.internet_users_in_the_world_today
5895566559
```

Reload data to get the latest:

```python
>>> wc.reload_data()
>>> wc.world_population.current_population
8065300592
```

Get help and view information about mapped sections:

```python
>>> help(wc)
```


## worldometers.info

> Worldometer is run by an international team of developers, researchers, and volunteers with the goal of making world statistics available in a thought-provoking and time relevant format to a wide audience around the world. It is published by a small and independent digital media company based in the United States. We have no political, governmental, or corporate affiliation. Furthermore, we have no investors, donors, grants, or backers of any type. We are completely independent and self-financed through automated programmatic advertising sold in real time on multiple ad exchanges.

<p align="right">
    <sup><a href="https://www.worldometers.info/about/">worldometers.info/about</a></sup>
</p>


## Data Sources

> **[adapted]:** worldometers.info collects its statistics and data from the most reputable national and international organizations, including the United Nations, the World Health Organization, the Food and Agriculture Organization, OECD and others.
>
> Each Worldometer counter has its specific set of sources, which are listed on its dedicated page (accessible by clicking on the counter text link, when available).
>
> Data, estimates, and projections displayed on worldometers.info counters are for the most part provided by organizations included in the following list of United Nations Statistics Division's partners.

<p align="right">
    <sup><a href="https://www.worldometers.info/sources/">worldometers.info/sources</a></sup>
</p>


## Contributions

All contributions are welcome!

Found a problem, want to give a tip? [open an issue](https://github.com/matheusfelipeog/worldometer/issues)

Do you have a solution to the problem? [Send me a PR](https://github.com/matheusfelipeog/worldometer/pulls)

Did you like this project? [Click on the star ⭐](https://github.com/matheusfelipeog/worldometer/stargazers)


## License

This project is using the MIT license, see in [MIT LICENSE](https://github.com/matheusfelipeog/worldometer/blob/master/LICENSE).
