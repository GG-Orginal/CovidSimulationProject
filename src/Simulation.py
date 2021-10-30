# Contains the logic for the loop that
# executes the actual simulation
from InitialPopulation import *
from Person import Person

current_population = createPopulation()
user_input_initial_population_size = 20


# transmit method to see if the disease was transmitted between people
def transmit(person, neighbor):
    # check to see if the person is compliant and the neighbor is compliant
    # if so, drop out
    if person.is_compliant and neighbor.is_compliant:
        return

    # check to see if the neighbor is healthy and if the person is healthy
    # if so, drop out
    if not neighbor.is_infected and not person.is_infected:
        return

    # If both are already infected we will not transmit
    if neighbor.is_infected and person.is_infected:
        return

    # Generate a number that is less than 75, if so, it will return true
    random = randrange(100) < 75
    if random:
        # Possibility that the virus will be transmitted
        # Person.infected_counter += 1

        # At this point either person or neighbor is healthy
        # so we only want to change the one who is healthy to infected
        # to avoid double counting
        if person.is_healthy:
            person.changeToInfected()
        else:
            neighbor.changeToInfected()

        # person.is_infected = True
        # neighbor.is_infected = True
        # person.is_healthy = False
        # neighbor.is_healthy = False


# Initiates the Population
def initiatePopulation():
    # original_population_state = [[Person() for x in range(10)] for y in range (10)]
    # original_population_state = np.empty((10, 10), dtype=Person)
    original_population_state = createPopulation()
    return original_population_state


# Updates the Population
def updateStatus(initial_population):
    new_population_state = initial_population[:]
    # population_dimensions = int(InitialPopulation.user_input_initial_population_size)

    for i in range(len(new_population_state)):
        for j in range(len(new_population_state[i])):
            if initial_population[i][j].is_infected:
                if j < user_input_initial_population_size - 1:
                    transmit(initial_population[i][j], new_population_state[i][j + 1])
                if j > 0:
                    transmit(initial_population[i][j], new_population_state[i][j - 1])
                if i < user_input_initial_population_size - 1:
                    transmit(initial_population[i][j], new_population_state[i + 1][j])
                if i > 0:
                    transmit(initial_population[i][j], new_population_state[i - 1][j])

    Simulation.current_population = new_population_state[:]
    return new_population_state


def reset_population():
    Simulation.current_population = createPopulation()
    Person.reset_counters()


class Simulation:
    pass
