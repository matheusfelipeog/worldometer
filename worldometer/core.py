# -*- coding: utf-8 -*-

"""
worldometer.core
----------------

This module contains the core objects that power Worldometer.
"""


import re

from requests_html import HTML, HTMLSession


# Constant variables, used in the Worldometer module.

URL = 'https://www.worldometers.info/'

_CSS_SELECTOR_OF_COUNTER_NUMBERS = '.counter-number'
_CSS_SELECTOR_OF_COUNTER_ITEM = '.counter-item, .counter-item-double'

_METRICS_LABELS = {
    'world_population': [
        'current_world_population',
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
        'non-renewable_sources',
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
        'hiv/aids_infected_people',
        'deaths_caused_by_hiv/aids_this_year',
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


class Worldometer(object):
    """Worldometer - Get metrics from site https://www.worldometers.info"""

    def __init__(self, timeout: int = 15):
        """Initializer of Worldometer class.
        
        Keyword Arguments:

        `timeout: int` - timeout, in seconds, to wait for processing.
        """

        self.__r = None  # Stores the response with html code for later rendering

        self.__timeout = timeout

        self._metrics = self.collect_metrics()
        
    @property
    def metrics(self) -> list:
        """Get all metrics of worldometer."""

        return self._metrics

    def _get_html(self, url: str) -> str:
        """Get the html code from the specified url and
        return its rendered content.
        """

        session = HTMLSession()

        try:
            # Get html page and render dynamic content
            self.__r = session.get(url, timeout=self.__timeout)
            self.__r.html.render(timeout=self.__timeout)

            return self.__r.html.raw_html

        except Exception as err:
            raise Exception(err)

    @staticmethod
    def find_metrics_in_html(html_code: str) -> list:
        """Find worldometer metrics in html code.
        
        Keyword Arguments:

        `html_code: str` - Receive html code.
        
        `return: list` - A list of not sanitized metrics of str type.
        """

        html = HTML(html=html_code)

        # Get only text of all requests_html.Element object
        metrics = [metric.text for metric in html.find(_CSS_SELECTOR_OF_COUNTER_NUMBERS)]

        return metrics

    @staticmethod
    def sanitize_metrics(metric_list: list) -> list:
        """Sanitize all metrics in list.
        
        Keyword Arguments:

        `metric_list: list` - Receive list of metrics in str type.
        
        `return: list` - A list of sanitized metrics of int type.
        """

        sanitized_metrics = []

        for metric in metric_list:
            
            # Get only the number and convert to int
            found = re.search(r'[0-9,]+', metric).group()
            number = int(found.replace(',', ''))

            sanitized_metrics.append(number)
        
        return sanitized_metrics

    def collect_metrics(self) -> list:
        """Collects all metrics from the worldometer site.

        `return: list` - A list of metrics of int type.
        """

        if self.__r is None:
            html = self._get_html(url=URL)
        else:
            html = self.__r.html.raw_html

        metrics = self.find_metrics_in_html(html_code=html)
        sanitized_metrics = self.sanitize_metrics(metric_list=metrics)

        return sanitized_metrics

    def update_metrics(self) -> None:
        """Update metrics of worldometer."""

        if self.__r is not None:
            self.__r.html.render(timeout=self.__timeout)
            self._metrics = self.collect_metrics()
        else:
            raise Exception('There are no metrics. Collect them to update.')

    @staticmethod
    def metrics_labels(with_categories=False) -> list or dict:
        """Return metrics labels of worldometer.
        
        `with_categories: bool` - If True, return metrics labels in categories.

        `return: list or dict` - A list or dict of metrics labels.
        """

        if with_categories:
            return _METRICS_LABELS

        only_metrics = []
        for metrics in _METRICS_LABELS.values():
            only_metrics.extend(metrics)

        return only_metrics

    @staticmethod
    def categories() -> list:
        """Return categories of worldometer.
        
        `return` - A list of categories of str type.
        """

        return [category for category in _METRICS_LABELS.keys()]

    def metrics_with_labels(self, with_categories: bool = False) -> dict:
        """Return metrics with labels in key-value structure.
        
        `with_categories: bool` - If True, return metrics with labels in categories.

        `return` - Metrics with labels in dict structure.
        """

        metrics = self.metrics.copy()

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
