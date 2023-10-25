# -*- coding: utf-8 -*-

"""
worldometer.core
----------------

This module contains the core objects that power Worldometer.

Examples
--------
>>> from worldometer import core
>>> w = core.Worldometer()

See url of worldometers.info

>>> core.URL
'https://www.worldometers.info/'

Get the number of categories, labels and metrics in w object:

>>> w.what_is_here()
{'categories': 8, 'labels': 63, 'metrics': 63}

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
    ...: ...
}
"""

__all__ = ['Worldometer']

import warnings
from functools import wraps
from dataclasses import asdict

from worldometer.world import WorldCounters

# Constant variables, used in the Worldometer module.

URL = 'https://www.worldometers.info/'

_METRICS_LABELS = {
    'world_population': [
        'current_population',
        'births_this_year',
        'births_today',
        'deaths_this_year',
        'deaths_today',
        'net_population_growth_this_year',
        'net_population_growth_today'
    ],
    'government_and_economics': [
        'public_healthcare_expenditure_today',
        'public_education_expenditure_today',
        'public_military_expenditure_today',
        'cars_produced_this_year',
        'bicycles_produced_this_year',
        'computers_produced_this_year'
    ],
    'society_and_media': [
        'new_book_titles_published_this_year',
        'newspapers_circulated_today',
        'tv_sets_sold_worldwide_today',
        'cellular_phones_sold_today',
        'money_spent_on_videogames_today',
        'internet_users_in_the_world_today',
        'emails_sent_today',
        'blog_posts_written_today',
        'tweets_sent_today',
        'google_searches_today'
    ],
    'environment': [
        'forest_loss_this_year',
        'land_lost_to_soil_erosion_this_year',
        'co2_emissions_this_year',
        'desertification_this_year',
        'toxic_chemicals_released_in_the_environment_this_year',
    ],
    'food': [
        'undernourished_people_in_the_world',
        'overweight_people_in_the_world',
        'obese_people_in_the_world',
        'people_who_died_of_hunger_today',
        'money_spent_for_obesity_related_diseases_in_the_usa_today',
        'money_spent_on_weight_loss_programs_in_the_usa_today',
    ],
    'water': [
        'water_used_this_year',
        'deaths_caused_by_water_related_diseases_this_year',
        'people_with_no_access_to_a_safe_drinking_water_source',
    ],
    'energy': [
        'energy_used_today',
        'non_renewable_sources',
        'renewable_sources',
        'solar_energy_striking_earth_today',
        'oil_pumped_today',
        'oil_left',
        'days_to_the_end_of_oil',
        'natural_gas_left',
        'days_to_the_end_of_natural_gas',
        'coal_left',
        'days_to_the_end_of_coal'
    ],
    'health': [
        'communicable_disease_deaths_this_year',
        'seasonal_flu_deaths_this_year',
        'deaths_of_children_under_5_this_year',
        'abortions_this_year',
        'deaths_of_mothers_during_birth_this_year',
        'hiv_aids_infected_people',
        'deaths_caused_by_hiv_aids_this_year',
        'deaths_caused_by_cancer_this_year',
        'deaths_caused_by_malaria_this_year',
        'cigarettes_smoked_today',
        'deaths_caused_by_smoking_this_year',
        'deaths_caused_by_alcohol_this_year',
        'suicides_this_year',
        'money_spent_on_illegal_drugs_this_year',
        'road_traffic_accident_fatalities_this_year'
    ]
}


def _deprecated_api(func_or_class):
    @wraps(func_or_class)
    def decorated(*args, **kwargs):
        warnings.warn(
            f'{func_or_class.__name__}() is deprecated. Use WorldCounters() instead.'
            ' It will be removed in a future release.',
            DeprecationWarning,
            stacklevel=2
        )
        return func_or_class(*args, **kwargs)
    return decorated


@_deprecated_api
class Worldometer(object):
    """This is the core class of the worldometer module.

    All functions/methods of the worldometer module use
    this class to build a Worldometer Object to access the collected data.

    Get more info about its attributes/methods using the ``help`` function:

    Example
    -------
    >>> from worldometer import Worldometer
    >>> help(Worldometer)
    class Worldometer(builtins.object)
    |  Worldometer(timeout: int = 30)
    |
    |  (...)
    |
    |  Methods defined here:
    |
    |  __init__(self, timeout: int = 30)
    |      Initializer of Worldometer class.
    |
    |      Parameters
    |      ----------
    |      timeout
    |         Seconds of wait for processing.
    |
    |   (...)
    """

    def __init__(self, timeout: int = 30):
        """Initializer of Worldometer class.

        Parameters
        ----------
        timeout
           Seconds of wait for processing.
        """
        self.__r = None  # Stores the response with html code for later rendering

        self.__timeout = timeout

        self._metrics = self.collect_metrics()

    def __str__(self):
        c, l, m = self.what_is_here().values()

        return f'Worldometer has {c} categories, {l} labels and {m} metrics'

    def __repr__(self):
        c, l, m = self.what_is_here().values()

        return (
            '<worldometer.Worldometer Object'
            f'(categories={c}, labels={l}, metrics={m})>'
        )

    def metrics(self) -> list:
        """Get all metrics of worldometer.

        Returns
        -------
        list
            A list with all metrics of woldometer.

        Example
        -------
        >>> from worldometer import Worldometer
        >>> w = Worldometer()
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
        """
        return self._metrics.copy()

    def _get_html(self, url: str) -> None:
        """Get the html code from the specified url and
        return its rendered content.
        """

    @staticmethod
    def find_metrics_in_html(html_code: str) -> None:
        """Find worldometer metrics in html code.

        Parameters
        ----------
        html_code
            Receive html code.

        Returns
        -------
        list
            A list of not sanitized metrics of str type.
        """

    @staticmethod
    def sanitize_metrics(metric_list: list) -> None:
        """Sanitize all metrics in list.

        Parameters
        ----------
        metric_list
            Receive list of metrics in str type.

        Returns
        -------
        list
            A list of sanitized metrics of int type.
        """

    def collect_metrics(self) -> list:
        """Collects all metrics from the worldometer site.

        Returns
        -------
        list
            A list of metrics of int type.
        """
        wc = WorldCounters()

        metrics = {
            **asdict(wc.world_population),
            **asdict(wc.government_and_economics),
            **asdict(wc.society_and_media),
            **asdict(wc.environment),
            **asdict(wc.food),
            **asdict(wc.water),
            **asdict(wc.energy),
            **asdict(wc.health)
        }

        metrics_values = list(metrics.values())

        return metrics_values

    def update_metrics(self) -> None:
        """Update metrics of worldometer."""
        self._metrics = self.collect_metrics()

    @staticmethod
    def metrics_labels(with_categories=False) -> list:
        """Return metrics labels of worldometer.

        Parameters
        ----------
        with_categories
            If True, return metrics labels in categories.

        Returns
        -------
        list
            A list of labels if ``with_categories`` parameter is False.

            A dict of labels with categories if ``with_categories`` parameter is True.

        Example
        -------
        >>> from worldometer import Worldometer
        >>> w = Worldometer()
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
        """
        if with_categories:
            return _METRICS_LABELS  # type: ignore

        only_metrics = []
        for metrics in _METRICS_LABELS.values():
            only_metrics.extend(metrics)

        return only_metrics

    @staticmethod
    def categories() -> list:
        """Return categories of worldometer.

        Returns
        -------
        list
            A list of categories of str type.

        Example
        -------
        >>> from worldometer import Worldometer
        >>> w = Worldometer()
        >>> w.categories()
        [
            'world_population',
            'government_and_economics',
            'society_and_media',
            ...
        ]
        """
        return [category for category in _METRICS_LABELS.keys()]

    def metrics_with_labels(self, with_categories: bool = False) -> dict:
        """Return metrics with labels in key-value structure.

        Parameters
        ----------
        with_categories
            If True, return metrics with labels in categories.

        Returns
        -------
        dict
            Metrics with labels in dict structure.

        Example
        -------
        >>> from worldometer import Worldometer
        >>> w = Worldometer()
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
        """
        metrics = self.metrics()

        if with_categories:

            m_with_l = {}  # Storage all structure of metrics with labels
            metrics_labels = self.metrics_labels(with_categories=True).copy()

            idx = 0  # Index for get metrics in idx position
            for category in metrics_labels:

                m_with_l[category] = {}  # Each category has a dict structure

                for label in metrics_labels[category]:

                    # Storage of a metric on the key label as the index
                    # increases +1 to iterate through the entire list of metrics
                    m_with_l[category][label] = metrics[idx]
                    idx += 1

            return m_with_l

        else:

            labels = self.metrics_labels().copy()

            return dict(
                zip(labels, metrics)
            )

    def what_is_here(self) -> dict:
        """Return what is here in object.

        Returns
        -------
        dict
            Number of categories, labels and metrics.

        Example
        -------
        >>> from worldometer import Worldometer
        >>> w = Worldometer()
        >>> w.what_is_here()
        {'categories': 8, 'labels': 63, 'metrics': 63}
        """
        return {
            'categories': len(self.categories()),
            'labels': len(self.metrics_labels()),
            'metrics': len(self.metrics())
        }
