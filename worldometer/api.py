# -*- coding: utf-8 -*-

"""
worldometer.api
---------------

Implementation of a simplified API of the worldometer module.

Here you will find all the functions available to obtain the metrics separately.

Examples
--------
>>> from worldometer import api

All worldometer.api functions use the ``get_metric_of`` function at their core.
To use it, just enter the corresponding label:

>>> api.get_metric_of(label='computers_produced_this_year')
{'computers_produced_this_year': 27760858}

There is also a simplified and self-explanatory API that provides
functions corresponding to the labels.
Autocomplete tools from the editors/IDE will help you use these
functions without having to decorate all labels:

>>> api.current_world_population()
{'current_world_population': 7845085923}

>>> api.tweets_sent_today()
{'tweets_sent_today': 4539558}
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

from worldometer import Worldometer
from worldometer.core import _deprecated_api


_cached_metrics = {}


@_deprecated_api
def get_metric_of(label: str) -> dict:
    """Get metric of label specified.

    Parameters
    ----------
    label
        Label of metric.

    Returns
    -------
    dict
        Label with metric in dict format.

    Example
    -------
    >>> get_metric_of(label='current_world_population')
    {'current_world_population': 7845085923}
    """

    if not _cached_metrics:
        w = Worldometer()
        _cached_metrics.update(w.metrics_with_labels())

    metrics = _cached_metrics.copy()

    if label not in metrics:
        raise Exception(f'This label "{label}" is invalid, please use a valid label.')

    return {label: metrics[label]}


@_deprecated_api
def update_metrics() -> None:
    """Update metrics of worldometer."""
    _cached_metrics.clear()


@_deprecated_api
def current_world_population() -> dict:
    """Get number of current world population."""
    return get_metric_of(label='current_population')


@_deprecated_api
def births_this_year() -> dict:
    """Get number of births this year."""
    return get_metric_of(label='births_this_year')


@_deprecated_api
def births_today() -> dict:
    """Get number of births today."""
    return get_metric_of(label='births_today')


@_deprecated_api
def deaths_this_year() -> dict:
    """Get number of deaths this year."""
    return get_metric_of(label='deaths_this_year')


@_deprecated_api
def deaths_today() -> dict:
    """Get number of deaths today."""
    return get_metric_of(label='deaths_today')


@_deprecated_api
def net_population_growth_this_year() -> dict:
    """Get number of net population growth this year."""
    return get_metric_of(label='net_population_growth_this_year')


@_deprecated_api
def net_population_growth_today() -> dict:
    """Get number of net population growth today."""
    return get_metric_of(label='net_population_growth_today')


@_deprecated_api
def public_healthcare_expenditure_today() -> dict:
    """Get number of public healthcare expenditure today."""
    return get_metric_of(label='public_healthcare_expenditure_today')


@_deprecated_api
def public_education_expenditure_today() -> dict:
    """Get number of public education expenditure today."""
    return get_metric_of(label='public_education_expenditure_today')


@_deprecated_api
def public_military_expenditure_today() -> dict:
    """Get number of public military expenditure today."""
    return get_metric_of(label='public_military_expenditure_today')


@_deprecated_api
def cars_produced_this_year() -> dict:
    """Get number of cars produced this year."""
    return get_metric_of(label='cars_produced_this_year')


@_deprecated_api
def bicycles_produced_this_year() -> dict:
    """Get number of bicycles produced this year."""
    return get_metric_of(label='bicycles_produced_this_year')


@_deprecated_api
def computers_produced_this_year() -> dict:
    """Get number of computers produced this year."""
    return get_metric_of(label='computers_produced_this_year')


@_deprecated_api
def new_book_titles_published_this_year() -> dict:
    """Get number of new book titles published this year."""
    return get_metric_of(label='new_book_titles_published_this_year')


@_deprecated_api
def newspapers_circulated_today() -> dict:
    """Get number of newspapers circulated today."""
    return get_metric_of(label='newspapers_circulated_today')


@_deprecated_api
def tv_sets_sold_worldwide_today() -> dict:
    """Get number of tv sets sold worldwide today."""
    return get_metric_of(label='tv_sets_sold_worldwide_today')


@_deprecated_api
def cellular_phones_sold_today() -> dict:
    """Get number of cellular phones sold today."""
    return get_metric_of(label='cellular_phones_sold_today')


@_deprecated_api
def money_spent_on_videogames_today() -> dict:
    """Get number of money spent on videogames today."""
    return get_metric_of(label='money_spent_on_videogames_today')


@_deprecated_api
def internet_users_in_the_world_today() -> dict:
    """Get number of internet users in the world today."""
    return get_metric_of(label='internet_users_in_the_world_today')


@_deprecated_api
def emails_sent_today() -> dict:
    """Get number of emails sent today."""
    return get_metric_of(label='emails_sent_today')


@_deprecated_api
def blog_posts_written_today() -> dict:
    """Get number of blog posts written today."""
    return get_metric_of(label='blog_posts_written_today')


@_deprecated_api
def tweets_sent_today() -> dict:
    """Get number of tweets sent today."""
    return get_metric_of(label='tweets_sent_today')


@_deprecated_api
def google_searches_today() -> dict:
    """Get number of google searches today."""
    return get_metric_of(label='google_searches_today')


@_deprecated_api
def forest_loss_this_year() -> dict:
    """Get number of forest loss this year."""
    return get_metric_of(label='forest_loss_this_year')


@_deprecated_api
def land_lost_to_soil_erosion_this_year() -> dict:
    """Get number of land lost to soil erosion this year."""
    return get_metric_of(label='land_lost_to_soil_erosion_this_year')


@_deprecated_api
def co2_emissions_this_year() -> dict:
    """Get number of co2 emissions this year."""
    return get_metric_of(label='co2_emissions_this_year')


@_deprecated_api
def desertification_this_year() -> dict:
    """Get number of desertification this year."""
    return get_metric_of(label='desertification_this_year')


@_deprecated_api
def toxic_chemicals_released_in_the_environment_this_year() -> dict:
    """Get number of toxic chemicals released in the environment this year."""
    return get_metric_of(label='toxic_chemicals_released_in_the_environment_this_year')


@_deprecated_api
def undernourished_people_in_the_world() -> dict:
    """Get number of undernourished people in the world."""
    return get_metric_of(label='undernourished_people_in_the_world')


@_deprecated_api
def overweight_people_in_the_world() -> dict:
    """Get number of overweight people in the world."""
    return get_metric_of(label='overweight_people_in_the_world')


@_deprecated_api
def obese_people_in_the_world() -> dict:
    """Get number of obese people in the world."""
    return get_metric_of(label='obese_people_in_the_world')


@_deprecated_api
def people_who_died_of_hunger_today() -> dict:
    """Get number of people who died of hunger today."""
    return get_metric_of(label='people_who_died_of_hunger_today')


@_deprecated_api
def money_spent_for_obesity_related_diseases_in_the_usa_today() -> dict:
    """Get number of money spent for obesity related diseases in the usa today."""
    return get_metric_of(label='money_spent_for_obesity_related_diseases_in_the_usa_today')


@_deprecated_api
def money_spent_on_weight_loss_programs_in_the_usa_today() -> dict:
    """Get number of money spent on weight loss programs in the usa today."""
    return get_metric_of(label='money_spent_on_weight_loss_programs_in_the_usa_today')


@_deprecated_api
def water_used_this_year() -> dict:
    """Get number of water used this year."""
    return get_metric_of(label='water_used_this_year')


@_deprecated_api
def deaths_caused_by_water_related_diseases_this_year() -> dict:
    """Get number of deaths caused by water related diseases this year."""
    return get_metric_of(label='deaths_caused_by_water_related_diseases_this_year')


@_deprecated_api
def people_with_no_access_to_a_safe_drinking_water_source() -> dict:
    """Get number of people with no access to a safe drinking water source."""
    return get_metric_of(label='people_with_no_access_to_a_safe_drinking_water_source')


@_deprecated_api
def energy_used_today() -> dict:
    """Get number of energy used today."""
    return get_metric_of(label='energy_used_today')


@_deprecated_api
def non_renewable_sources() -> dict:
    """Get number of non renewable sources."""
    return get_metric_of(label='non_renewable_sources')


@_deprecated_api
def renewable_sources() -> dict:
    """Get number of renewable sources."""
    return get_metric_of(label='renewable_sources')


@_deprecated_api
def solar_energy_striking_earth_today() -> dict:
    """Get number of solar energy striking earth today."""
    return get_metric_of(label='solar_energy_striking_earth_today')


@_deprecated_api
def oil_pumped_today() -> dict:
    """Get number of oil pumped today."""
    return get_metric_of(label='oil_pumped_today')


@_deprecated_api
def oil_left() -> dict:
    """Get number of oil left."""
    return get_metric_of(label='oil_left')


@_deprecated_api
def days_to_the_end_of_oil() -> dict:
    """Get number of days to the end of oil."""
    return get_metric_of(label='days_to_the_end_of_oil')


@_deprecated_api
def natural_gas_left() -> dict:
    """Get number of natural gas left."""
    return get_metric_of(label='natural_gas_left')


@_deprecated_api
def days_to_the_end_of_natural_gas() -> dict:
    """Get number of days to the end of natural gas."""
    return get_metric_of(label='days_to_the_end_of_natural_gas')


@_deprecated_api
def coal_left() -> dict:
    """Get number of coal left."""
    return get_metric_of(label='coal_left')


@_deprecated_api
def days_to_the_end_of_coal() -> dict:
    """Get number of days to the end of coal."""
    return get_metric_of(label='days_to_the_end_of_coal')


@_deprecated_api
def communicable_disease_deaths_this_year() -> dict:
    """Get number of communicable disease deaths this year."""
    return get_metric_of(label='communicable_disease_deaths_this_year')


@_deprecated_api
def seasonal_flu_deaths_this_year() -> dict:
    """Get number of seasonal flu deaths this year."""
    return get_metric_of(label='seasonal_flu_deaths_this_year')


@_deprecated_api
def deaths_of_children_under_5_this_year() -> dict:
    """Get number of deaths of children under 5 this year."""
    return get_metric_of(label='deaths_of_children_under_5_this_year')


@_deprecated_api
def abortions_this_year() -> dict:
    """Get number of abortions this year."""
    return get_metric_of(label='abortions_this_year')


@_deprecated_api
def deaths_of_mothers_during_birth_this_year() -> dict:
    """Get number of deaths of mothers during birth this year."""
    return get_metric_of(label='deaths_of_mothers_during_birth_this_year')


@_deprecated_api
def hiv_aids_infected_people() -> dict:
    """Get number of hiv aids infected people."""
    return get_metric_of(label='hiv_aids_infected_people')


@_deprecated_api
def deaths_caused_by_hiv_aids_this_year() -> dict:
    """Get number of deaths caused by hiv aids this year."""
    return get_metric_of(label='deaths_caused_by_hiv_aids_this_year')


@_deprecated_api
def deaths_caused_by_cancer_this_year() -> dict:
    """Get number of deaths caused by cancer this year."""
    return get_metric_of(label='deaths_caused_by_cancer_this_year')


@_deprecated_api
def deaths_caused_by_malaria_this_year() -> dict:
    """Get number of deaths caused by malaria this year."""
    return get_metric_of(label='deaths_caused_by_malaria_this_year')


@_deprecated_api
def cigarettes_smoked_today() -> dict:
    """Get number of cigarettes smoked today."""
    return get_metric_of(label='cigarettes_smoked_today')


@_deprecated_api
def deaths_caused_by_smoking_this_year() -> dict:
    """Get number of deaths caused by smoking this year."""
    return get_metric_of(label='deaths_caused_by_smoking_this_year')


@_deprecated_api
def deaths_caused_by_alcohol_this_year() -> dict:
    """Get number of deaths caused by alcohol this year."""
    return get_metric_of(label='deaths_caused_by_alcohol_this_year')


@_deprecated_api
def suicides_this_year() -> dict:
    """Get number of suicides this year."""
    return get_metric_of(label='suicides_this_year')


@_deprecated_api
def money_spent_on_illegal_drugs_this_year() -> dict:
    """Get number of money spent on illegal drugs this year."""
    return get_metric_of(label='money_spent_on_illegal_drugs_this_year')


@_deprecated_api
def road_traffic_accident_fatalities_this_year() -> dict:
    """Get number of road traffic accident fatalities this year."""
    return get_metric_of(label='road_traffic_accident_fatalities_this_year')
