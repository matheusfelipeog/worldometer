# -*- coding: utf-8 -*-

"""
worldometer.api
---------------

Implement a simplified api of worldometer.Worldometer Class.

API usage:

>>> from worldometer import api

>>> api.current_world_population()
{'current_world_population': 7845085923}

>>> api.tweets_sent_today()
{'tweets_sent_today': 4539558}

>>> api.get_metric_of(label='computers_produced_this_year')
{'computers_produced_this_year': 27760858}

More info in: github.com/matheusfelipeog/worldometer
"""


__all__ = [
    'get_metric_of',
    'update_metrics',
    'current_world_population',
    'births_this_year',
    'births_today',
    'deaths_this_year',
    'deaths_today',
    'net_population_growth_this_year',
    'net_population_growth_today',
    'public_healthcare_expenditure_today',
    'public_education_expenditure_today',
    'public_military_expenditure_today',
    'cars_produced_this_year',
    'bicycles_produced_this_year',
    'computers_produced_this_year',
    'new_book_titles_published_this_year',
    'newspapers_circulated_today',
    'tv_sets_sold_worldwide_today',
    'cellular_phones_sold_today',
    'money_spent_on_videogames_today',
    'internet_users_in_the_world_today',
    'emails_sent_today',
    'blog_posts_written_today',
    'tweets_sent_today',
    'google_searches_today',
    'forest_loss_this_year',
    'land_lost_to_soil_erosion_this_year',
    'co2_emissions_this_year',
    'desertification_this_year',
    'toxic_chemicals_released_in_the_environment_this_year',
    'undernourished_people_in_the_world',
    'overweight_people_in_the_world',
    'obese_people_in_the_world',
    'people_who_died_of_hunger_today',
    'money_spent_for_obesity_related_diseases_in_the_usa_today',
    'money_spent_on_weight_loss_programs_in_the_usa_today',
    'water_used_this_year',
    'deaths_caused_by_water_related_diseases_this_year',
    'people_with_no_access_to_a_safe_drinking_water_source',
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
    'days_to_the_end_of_coal',
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


from .core import Worldometer

from .__about__ import __version__, __author__, __email__


__w = Worldometer()


def get_metric_of(label: str) -> dict:
    """Get metric of label specified.
    
    Keyword Argument:

    `label: str` - Label of metric.

    `return: dict` - Label with metric in dict format.

    Usage:

    >>> get_metric_of(label='current_world_population')
    {'current_world_population': 7845085923}
    """

    metrics = __w.metrics_with_labels()

    if label not in metrics:
        raise Exception(f'This label "{label}" is invalid, please use a valid label.')

    return {label: metrics[label]}


def update_metrics() -> None:
    """Update metrics of worldometer."""
    
    __w.update_metrics()


def current_world_population() -> int:
    return get_metric_of(label='current_world_population')


def births_this_year() -> int:
    return get_metric_of(label='births_this_year')


def births_today() -> int:
    return get_metric_of(label='births_today')


def deaths_this_year() -> int:
    return get_metric_of(label='deaths_this_year')


def deaths_today() -> int:
    return get_metric_of(label='deaths_today')


def net_population_growth_this_year() -> int:
    return get_metric_of(label='net_population_growth_this_year')


def net_population_growth_today() -> int:
    return get_metric_of(label='net_population_growth_today')


def public_healthcare_expenditure_today() -> int:
    return get_metric_of(label='public_healthcare_expenditure_today')


def public_education_expenditure_today() -> int:
    return get_metric_of(label='public_education_expenditure_today')


def public_military_expenditure_today() -> int:
    return get_metric_of(label='public_military_expenditure_today')


def cars_produced_this_year() -> int:
    return get_metric_of(label='cars_produced_this_year')


def bicycles_produced_this_year() -> int:
    return get_metric_of(label='bicycles_produced_this_year')


def computers_produced_this_year() -> int:
    return get_metric_of(label='computers_produced_this_year')


def new_book_titles_published_this_year() -> int:
    return get_metric_of(label='new_book_titles_published_this_year')


def newspapers_circulated_today() -> int:
    return get_metric_of(label='newspapers_circulated_today')


def tv_sets_sold_worldwide_today() -> int:
    return get_metric_of(label='tv_sets_sold_worldwide_today')


def cellular_phones_sold_today() -> int:
    return get_metric_of(label='cellular_phones_sold_today')


def money_spent_on_videogames_today() -> int:
    return get_metric_of(label='money_spent_on_videogames_today')


def internet_users_in_the_world_today() -> int:
    return get_metric_of(label='internet_users_in_the_world_today')


def emails_sent_today() -> int:
    return get_metric_of(label='emails_sent_today')


def blog_posts_written_today() -> int:
    return get_metric_of(label='blog_posts_written_today')


def tweets_sent_today() -> int:
    return get_metric_of(label='tweets_sent_today')


def google_searches_today() -> int:
    return get_metric_of(label='google_searches_today')


def forest_loss_this_year() -> int:
    return get_metric_of(label='forest_loss_this_year')


def land_lost_to_soil_erosion_this_year() -> int:
    return get_metric_of(label='land_lost_to_soil_erosion_this_year')


def co2_emissions_this_year() -> int:
    return get_metric_of(label='co2_emissions_this_year')


def desertification_this_year() -> int:
    return get_metric_of(label='desertification_this_year')


def toxic_chemicals_released_in_the_environment_this_year() -> int:
    return get_metric_of(label='toxic_chemicals_released_in_the_environment_this_year')


def undernourished_people_in_the_world() -> int:
    return get_metric_of(label='undernourished_people_in_the_world')


def overweight_people_in_the_world() -> int:
    return get_metric_of(label='overweight_people_in_the_world')


def obese_people_in_the_world() -> int:
    return get_metric_of(label='obese_people_in_the_world')


def people_who_died_of_hunger_today() -> int:
    return get_metric_of(label='people_who_died_of_hunger_today')


def money_spent_for_obesity_related_diseases_in_the_usa_today() -> int:
    return get_metric_of(label='money_spent_for_obesity_related_diseases_in_the_usa_today')


def money_spent_on_weight_loss_programs_in_the_usa_today() -> int:
    return get_metric_of(label='money_spent_on_weight_loss_programs_in_the_usa_today')


def water_used_this_year() -> int:
    return get_metric_of(label='water_used_this_year')


def deaths_caused_by_water_related_diseases_this_year() -> int:
    return get_metric_of(label='deaths_caused_by_water_related_diseases_this_year')


def people_with_no_access_to_a_safe_drinking_water_source() -> int:
    return get_metric_of(label='people_with_no_access_to_a_safe_drinking_water_source')


def energy_used_today() -> int:
    return get_metric_of(label='energy_used_today')


def non_renewable_sources() -> int:
    return get_metric_of(label='non-renewable_sources')


def renewable_sources() -> int:
    return get_metric_of(label='renewable_sources')


def solar_energy_striking_earth_today() -> int:
    return get_metric_of(label='solar_energy_striking_earth_today')


def oil_pumped_today() -> int:
    return get_metric_of(label='oil_pumped_today')


def oil_left() -> int:
    return get_metric_of(label='oil_left')


def days_to_the_end_of_oil() -> int:
    return get_metric_of(label='days_to_the_end_of_oil')


def natural_gas_left() -> int:
    return get_metric_of(label='natural_gas_left')


def days_to_the_end_of_natural_gas() -> int:
    return get_metric_of(label='days_to_the_end_of_natural_gas')


def coal_left() -> int:
    return get_metric_of(label='coal_left')


def days_to_the_end_of_coal() -> int:
    return get_metric_of(label='days_to_the_end_of_coal')


def communicable_disease_deaths_this_year() -> int:
    return get_metric_of(label='communicable_disease_deaths_this_year')


def seasonal_flu_deaths_this_year() -> int:
    return get_metric_of(label='seasonal_flu_deaths_this_year')


def deaths_of_children_under_5_this_year() -> int:
    return get_metric_of(label='deaths_of_children_under_5_this_year')


def abortions_this_year() -> int:
    return get_metric_of(label='abortions_this_year')


def deaths_of_mothers_during_birth_this_year() -> int:
    return get_metric_of(label='deaths_of_mothers_during_birth_this_year')


def hiv_aids_infected_people() -> int:
    return get_metric_of(label='hiv/aids_infected_people')


def deaths_caused_by_hiv_aids_this_year() -> int:
    return get_metric_of(label='deaths_caused_by_hiv/aids_this_year')


def deaths_caused_by_cancer_this_year() -> int:
    return get_metric_of(label='deaths_caused_by_cancer_this_year')


def deaths_caused_by_malaria_this_year() -> int:
    return get_metric_of(label='deaths_caused_by_malaria_this_year')


def cigarettes_smoked_today() -> int:
    return get_metric_of(label='cigarettes_smoked_today')


def deaths_caused_by_smoking_this_year() -> int:
    return get_metric_of(label='deaths_caused_by_smoking_this_year')


def deaths_caused_by_alcohol_this_year() -> int:
    return get_metric_of(label='deaths_caused_by_alcohol_this_year')


def suicides_this_year() -> int:
    return get_metric_of(label='suicides_this_year')


def money_spent_on_illegal_drugs_this_year() -> int:
    return get_metric_of(label='money_spent_on_illegal_drugs_this_year')


def road_traffic_accident_fatalities_this_year() -> int:
    return get_metric_of(label='road_traffic_accident_fatalities_this_year')
