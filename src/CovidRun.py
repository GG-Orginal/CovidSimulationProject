from InitialPopulation import createPopulation
from Person import Person
from Simulation import updateStatus


def print_stats(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            is_infected = state[i][j].is_infected
            is_not_compliant = not state[i][j].is_compliant
            if is_infected:
                Person.infected_counter += 1
            if is_not_compliant:
                Person.non_compliance_counter += 1
    print("Number of Infected: " + str(Person.infected_counter))
    print("Number of Non-Compliance: " + str(Person.non_compliance_counter))
    Person.infected_counter = 0
    Person.non_compliance_counter = 0
    print("------------------------------------------------------------------------------------")


class CovidRun:
    print("Day: 0")
    original_population_state = createPopulation()
    for i in range(len(original_population_state)):
        for j in range(len(original_population_state[i])):
            is_infected = original_population_state[i][j].is_infected
            is_not_compliant = not original_population_state[i][j].is_compliant
            if is_infected:
                Person.infected_counter += 1
            if is_not_compliant:
                Person.non_compliance_counter += 1
    print("Number of Infected: " + str(Person.infected_counter))
    print("Number of Non-Compliance: " + str(Person.non_compliance_counter))
    Person.infected_counter = 0
    Person.non_compliance_counter = 0
    print("------------------------------------------------------------------------------------")

    for x in range(100):
        print("Day: " + str(x + 1))
        original_population_state = updateStatus(original_population_state)
        print_stats(original_population_state)
