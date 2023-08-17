class WorldPopulation:

    def __init__(self) -> None:
        self._data = self._load_data()
        self.current_population = self._data.get('current_population')
        self.births_today = self._data.get('births_today')
        self.births_this_year = self._data.get('births_this_year')
        self.deaths_today = self._data.get('dth1s_today')
        self.deaths_this_year = self._data.get('dth1s_this_year')
        self.net_population_growth_today = self._data.get('absolute_growth')
        self.net_population_growth_this_year = self._data.get('absolute_growth_year')

    def _load_data(self) -> dict:
        return {}


class GovernmentAndEconomics:

    def __init__(self) -> None:
        self._data = self._load_data()
        self.public_healthcare_expenditure_today = self._data.get('gov_expenditures_health')
        self.public_education_expenditure_today = self._data.get('gov_expenditures_education')
        self.public_military_expenditure_today = self._data.get('gov_expenditures_military')
        self.cars_produced_this_year = self._data.get('automobile_produced')
        self.bicycles_produced_this_year = self._data.get('bicycle_produced')
        self.computers_produced_this_year = self._data.get('computers_sold')

    def _load_data(self) -> dict:
        return {}


class SocietyAndMedia:

    def __init__(self) -> None:
        self._data = self._load_data()
        self.new_book_titles_published_this_year = self._data.get('books_published')
        self.newspapers_circulated_today = self._data.get('newspapers_circulated')
        self.tv_sets_sold_worldwide_today = self._data.get('tv')
        self.cellular_phones_sold_today = self._data.get('cellular')
        self.money_spent_on_videogames_today = self._data.get('videogames')
        self.internet_users_in_the_world_today = self._data.get('internet_users')
        self.emails_sent_today = self._data.get('em')
        self.blog_posts_written_today = self._data.get('blog_posts')
        self.tweets_sent_today = self._data.get('tweets')
        self.google_searches_today = self._data.get('google_searches')

    def _load_data(self) -> dict:
        return {}


class Environment:

    def __init__(self) -> None:
        self._data = self._load_data()
        self.forest_loss_this_year = self._data.get('forest_loss')
        self.land_lost_to_soil_erosion_this_year = self._data.get('soil_erosion')
        self.co2_emissions_this_year = self._data.get('co2_emissions')
        self.desertification_this_year = self._data.get('desert_land_formed')
        self.toxic_chemicals_released_in_the_environment_this_year = self._data.get('tox_chem')

    def _load_data(self) -> dict:
        return {}


class Food:

    def __init__(self) -> None:
        self._data = self._load_data()
        self.undernourished_people_in_the_world = self._data.get('undernourished')
        self.overweight_people_in_the_world = self._data.get('overweight')
        self.obese_people_in_the_world = self._data.get('obese')
        self.people_who_died_of_hunger_today = self._data.get('dth1_hunger')
        self.money_spent_for_obesity_related_diseases_in_the_usa_today = self._data.get('obesity_spending')
        self.money_spent_on_weight_loss_programs_in_the_usa_today = self._data.get('spending_on_weight_loss')

    def _load_data(self) -> dict:
        return {}


class Water:

    def __init__(self) -> None:
        self._data = self._load_data()
        self.water_used_this_year = self._data.get('water_consumed')
        self.deaths_caused_by_water_related_diseases_this_year = self._data.get('water_disax')
        self.people_with_no_access_to_a_safe_drinking_water_source = self._data.get('nowater_population')

    def _load_data(self) -> dict:
        return {}


class Energy:

    def __init__(self) -> None:
        self._data = self._load_data()
        self.energy_used_today = self._data.get('energy_used')
        self.non_renewable_sources = self._data.get('energy_nonren')
        self.renewable_sources = self._data.get('energy_ren')
        self.solar_energy_striking_earth_today = self._data.get('solar_energy')
        self.oil_pumped_today = self._data.get('oil_consumption')
        self.oil_left = self._data.get('oil_reserves')
        self.days_to_the_end_of_oil = self._data.get('oil_days')
        self.natural_gas_left = self._data.get('gas_reserves')
        self.days_to_the_end_of_natural_gas = self._data.get('gas_days')
        self.coal_left = self._data.get('coal_reserves')
        self.days_to_the_end_of_coal = self._data.get('coal_days')

    def _load_data(self) -> dict:
        return {}


class Health:

    def __init__(self) -> None:
        self._data = self._load_data()
        self.communicable_disease_deaths_this_year = self._data.get('dth1s_communicable_disaxs')
        self.seasonal_flu_deaths_this_year = self._data.get('dth1s_flu')
        self.deaths_of_children_under_5_this_year = self._data.get('dth1s_children')
        self.abortions_this_year = self._data.get('ab')
        self.deaths_of_mothers_during_birth_this_year = self._data.get('dth1s_maternal')
        self.hiv_aids_infected_people = self._data.get('infections_hiv')
        self.deaths_caused_by_hiv_aids_this_year = self._data.get('dth1s_ads')
        self.deaths_caused_by_cancer_this_year = self._data.get('dth1s_cancer')
        self.deaths_caused_by_malaria_this_year = self._data.get('dth1s_malarial')
        self.cigarettes_smoked_today = self._data.get('cigarettes_smoked')
        self.deaths_caused_by_smoking_this_year = self._data.get('dth1s_cigarettes')
        self.deaths_caused_by_alcohol_this_year = self._data.get('dth1s_alchool')
        self.suicides_this_year = self._data.get('sui')
        self.money_spent_on_illegal_drugs_this_year = self._data.get('drug_spending')
        self.road_traffic_accident_fatalities_this_year = self._data.get('dth1s_cars')

    def _load_data(self) -> dict:
        return {}
