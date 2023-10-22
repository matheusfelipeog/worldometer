"""
worldometer package
-------------------

The `worldometer` package accesses various counters and live data available
throughout the https://www.worldometers.info website and provides them
through self-describing classes, methods and attributes.

Examples
--------
Get the data from the live counters available on the homepage::

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

Notes
-----
Check https://www.worldometers.info/about for more information about
the data source, how live counters work, and more related information.
"""

__all__ = [
    'Worldometer',
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

__version__ = '2.0.0'
__author__ = 'Matheus Felipe'

# TODO: The worldometer.core module is deprecated.
# TODO: The old API (worldometer.api) is deprecated.
# This will be removed in the future.
from worldometer.core import Worldometer
from worldometer.api import (
    get_metric_of,
    update_metrics,
    current_world_population,
    births_this_year,
    births_today,
    deaths_this_year,
    deaths_today,
    net_population_growth_this_year,
    net_population_growth_today,
    public_healthcare_expenditure_today,
    public_education_expenditure_today,
    public_military_expenditure_today,
    cars_produced_this_year,
    bicycles_produced_this_year,
    computers_produced_this_year,
    new_book_titles_published_this_year,
    newspapers_circulated_today,
    tv_sets_sold_worldwide_today,
    cellular_phones_sold_today,
    money_spent_on_videogames_today,
    internet_users_in_the_world_today,
    emails_sent_today,
    blog_posts_written_today,
    tweets_sent_today,
    google_searches_today,
    forest_loss_this_year,
    land_lost_to_soil_erosion_this_year,
    co2_emissions_this_year,
    desertification_this_year,
    toxic_chemicals_released_in_the_environment_this_year,
    undernourished_people_in_the_world,
    overweight_people_in_the_world,
    obese_people_in_the_world,
    people_who_died_of_hunger_today,
    money_spent_for_obesity_related_diseases_in_the_usa_today,
    money_spent_on_weight_loss_programs_in_the_usa_today,
    water_used_this_year,
    deaths_caused_by_water_related_diseases_this_year,
    people_with_no_access_to_a_safe_drinking_water_source,
    energy_used_today,
    non_renewable_sources,
    renewable_sources,
    solar_energy_striking_earth_today,
    oil_pumped_today,
    oil_left,
    days_to_the_end_of_oil,
    natural_gas_left,
    days_to_the_end_of_natural_gas,
    coal_left,
    days_to_the_end_of_coal,
    communicable_disease_deaths_this_year,
    seasonal_flu_deaths_this_year,
    deaths_of_children_under_5_this_year,
    abortions_this_year,
    deaths_of_mothers_during_birth_this_year,
    hiv_aids_infected_people,
    deaths_caused_by_hiv_aids_this_year,
    deaths_caused_by_cancer_this_year,
    deaths_caused_by_malaria_this_year,
    cigarettes_smoked_today,
    deaths_caused_by_smoking_this_year,
    deaths_caused_by_alcohol_this_year,
    suicides_this_year,
    money_spent_on_illegal_drugs_this_year,
    road_traffic_accident_fatalities_this_year
)
