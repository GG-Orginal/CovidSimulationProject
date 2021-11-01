from Person import *
from random import randrange

user_input_initial_infection_rate = 5
user_input_non_compliance_rate = 25
user_input_vaccination_rate = 10
user_input_initial_population_size = 20


def createPopulation():
    # This randomly determines if a person is healthy or not initially.
    def initial_health_stage():
        value_health = randrange(100) + 1
        if value_health > user_input_initial_infection_rate:
            is_healthy = True
        else:
            is_healthy = False
        return is_healthy

    # This randomly determines if a person is following social distancing or not.
    def compliance():
        value_non_compliance = randrange(100) + 1
        if value_non_compliance > user_input_non_compliance_rate:
            is_compliant = True
        else:
            is_compliant = False
        return is_compliant
    
    # This randomly determines if a person is vaccinated or not.
    def vaccination():
        value_non_vaccinated = randrange(100) + 1
        if value_non_vaccinated > user_input_vaccination_rate:
            is_vaccinated = False
        else:
            is_vaccinated = True
        return is_vaccinated

    # This is a list of all the individuals in the sample population
    population_array = [[Person() for j in range(user_input_initial_population_size)]
                        for i in range(user_input_initial_population_size)]

    # This will creates the initial population

    for i in range(len(population_array)):
        for j in range(len(population_array[i])):
            p1 = Person()
            p1.is_healthy = initial_health_stage()
            p1.is_infected = not initial_health_stage()
            p1.is_compliant = compliance()
            p1.is_vaccinated = vaccination()
            population_array[i][j] = p1
    return population_array


class InitialPopulation:
    pass
