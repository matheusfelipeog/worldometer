# -*- coding: utf-8 -*-

import re

from requests_html import HTML, HTMLSession


# Constant variables, used in the Worldometer module.

URL = 'https://www.worldometers.info/'

CSS_SELECTOR_OF_COUNTER_NUMBERS = '.counter-number'
CSS_SELECTOR_OF_COUNTER_ITEM = '.counter-item, .counter-item-double'

METRICS_LABELS = {
    'WORLD_POPULATION': [
        'current_world_population',
        'births_this_year',
        'births_today',
        'deaths_this_year',
        'deaths_today',
        'net_population_growth_this_year',
        'net_population_growth_today'
    ],
    'GOVERNMENT_AND_ECONOMICS': [
        'public_healthcare_expenditure_today',
        'public_education_expenditure_today',
        'public_military_expenditure_today',
        'cars_produced_this_year',
        'bicycles_produced_this_year',
        'computers_produced_this_year'
    ],
    'SOCIETY_AND_MEDIA': [
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
    'ENVIRONMENT': [
        'forest_loss_this_year',
        'land_lost_to_soil_erosion_this_year',
        'co2_emissions_this_year',
        'desertification_this_year',
        'toxic_chemicals_released_in_the_environment_this_year',
    ],
    'FOOD': [
        'undernourished_people_in_the_world',
        'overweight_people_in_the_world',
        'obese_people_in_the_world',
        'people_who_died_of_hunger_today',
        'money_spent_for_obesity_related_diseases_in_the_usa_today',
        'money_spent_on_weight_loss_programs_in_the_usa_today',
    ],
    'WATER': [
        'water_used_this_year',
        'deaths_caused_by_water_related_diseases_this_year',
        'people_with_no_access_to_a_safe_drinking_water_source',
    ],
    'ENERGY': [
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
    'HEALTH': [
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
    """Worldometer - Get metrics do site https://www.worldometers.info"""

    def __init__(self):
        self.metrics = self.collect_metrics()
        
    @staticmethod
    def _get_html(url: str) -> str:
        """Get the html code from the specified url and
        return its rendered content.
        """

        session = HTMLSession()
        timeout = 15  # in seconds

        try:
            # Get html page and render dynamic content
            r = session.get(url, timeout=timeout)
            r.html.render(timeout=timeout)

            return r.html.raw_html

        except Exception as err:
            raise Exception(err)

    @staticmethod
    def find_metrics_in_html(html_code: str) -> list:
        """Find worldometer metrics in html code."""

        html = HTML(html=html_code)

        # Get only text of all requests_html.Element object
        metrics = [metric.text for metric in html.find(CSS_SELECTOR_OF_COUNTER_NUMBERS)]

        return metrics

    @staticmethod
    def sanitize_metrics(metric_list: list) -> list:
        """Sanitize all metrics in list."""

        sanitized_metrics = []

        for metric in metric_list:
            
            # Get only the number and convert to int
            found = re.search(r'[0-9,]+', metric).group()
            number = int(found.replace(',', ''))

            sanitized_metrics.append(number)
        
        return sanitized_metrics

    def collect_metrics(self) -> list:
        """Collects all metrics from the worldometer site."""

        html = self._get_html(url=URL)
        metrics = self.find_metrics_in_html(html_code=html)
        sanitized_metrics = self.sanitize_metrics(metric_list=metrics)

        return sanitized_metrics
