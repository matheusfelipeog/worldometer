from dataclasses import dataclass, field

from typing import List, Union


@dataclass
class WorldPopulation:
    _data: dict = field(default_factory=dict, repr=False, init=False)
    current_population: Union[int, None] = None
    births_today: Union[int, None] = None
    births_this_year: Union[int, None] = None
    deaths_today: Union[int, None] = None
    deaths_this_year: Union[int, None] = None
    net_population_growth_today: Union[int, None] = None
    net_population_growth_this_year: Union[int, None] = None


@dataclass
class GovernmentAndEconomics:
    _data: dict = field(default_factory=dict, repr=False, init=False)
    public_healthcare_expenditure_today: Union[int, None] = None
    public_education_expenditure_today: Union[int, None] = None
    public_education_expenditure_today: Union[int, None] = None
    public_education_expenditure_today: Union[int, None] = None
    bicycles_produced_this_year: Union[int, None] = None
    computers_produced_this_year: Union[int, None] = None


@dataclass
class SocietyAndMedia:
    _data: dict = field(default_factory=dict, repr=False, init=False)
    new_book_titles_published_this_year: Union[int, None] = None
    newspapers_circulated_today: Union[int, None] = None
    tv_sets_sold_worldwide_today: Union[int, None] = None
    cellular_phones_sold_today: Union[int, None] = None
    money_spent_on_videogames_today: Union[int, None] = None
    internet_users_in_the_world_today: Union[int, None] = None
    emails_sent_today: Union[int, None] = None
    blog_posts_written_today: Union[int, None] = None
    tweets_sent_today: Union[int, None] = None
    google_searches_today: Union[int, None] = None


@dataclass
class Environment:
    _data: dict = field(default_factory=dict, repr=False, init=False)
    forest_loss_this_year: Union[int, None] = None
    land_lost_to_soil_erosion_this_year: Union[int, None] = None
    co2_emissions_this_year: Union[int, None] = None
    desertification_this_year: Union[int, None] = None
    toxic_chemicals_released_in_the_environment_this_year: Union[int, None] = None


@dataclass
class Food:
    _data: dict = field(default_factory=dict, repr=False, init=False)
    undernourished_people_in_the_world: Union[int, None] = None
    overweight_people_in_the_world: Union[int, None] = None
    obese_people_in_the_world: Union[int, None] = None
    people_who_died_of_hunger_today: Union[int, None] = None
    money_spent_for_obesity_related_diseases_in_the_usa_today: Union[int, None] = None
    money_spent_on_weight_loss_programs_in_the_usa_today: Union[int, None] = None


@dataclass
class Water:
    _data: dict = field(default_factory=dict, repr=False, init=False)
    water_used_this_year: Union[int, None] = None
    deaths_caused_by_water_related_diseases_this_year: Union[int, None] = None
    people_with_no_access_to_a_safe_drinking_water_source: Union[int, None] = None


@dataclass
class Energy:
    _data: dict = field(default_factory=dict, repr=False, init=False)
    energy_used_today: Union[int, None] = None
    non_renewable_sources: Union[int, None] = None
    renewable_sources: Union[int, None] = None
    solar_energy_striking_earth_today: Union[int, None] = None
    oil_pumped_today: Union[int, None] = None
    oil_left: Union[int, None] = None
    days_to_the_end_of_oil: Union[int, None] = None
    natural_gas_left: Union[int, None] = None
    days_to_the_end_of_natural_gas: Union[int, None] = None
    coal_left: Union[int, None] = None
    days_to_the_end_of_coal: Union[int, None] = None


@dataclass
class Health:
    _data: dict = field(default_factory=dict, repr=False, init=False)
    communicable_disease_deaths_this_year: Union[int, None] = None
    seasonal_flu_deaths_this_year: Union[int, None] = None
    deaths_of_children_under_5_this_year: Union[int, None] = None
    abortions_this_year: Union[int, None] = None
    deaths_of_mothers_during_birth_this_year: Union[int, None] = None
    hiv_aids_infected_people: Union[int, None] = None
    deaths_caused_by_hiv_aids_this_year: Union[int, None] = None
    deaths_caused_by_cancer_this_year: Union[int, None] = None
    deaths_caused_by_malaria_this_year: Union[int, None] = None
    cigarettes_smoked_today: Union[int, None] = None
    deaths_caused_by_smoking_this_year: Union[int, None] = None
    deaths_caused_by_alcohol_this_year: Union[int, None] = None
    suicides_this_year: Union[int, None] = None
    money_spent_on_illegal_drugs_this_year: Union[int, None] = None
    road_traffic_accident_fatalities_this_year: Union[int, None] = None


@dataclass
class CountryCodeData:
    country: str
    calling_code: str
    three_letter_iso: str
    two_letter_iso: str
    three_digit_iso_numeric: str


@dataclass
class CountryCodes:
    _data: List[CountryCodeData] = field(
        default_factory=list,
        repr=False,
        init=False
    )
