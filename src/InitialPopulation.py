from random import randrange
from src.Person import Person
from termcolor import colored

class Population:

    # This randomly determines if a person is healthy or not initially.
    def initial_health_stage(self):
        value_health = randrange(100) + 1
        if value_health > 5:
            is_healthy = True
        else:
            is_healthy = False
        return is_healthy

    # This randomly determines if a person is following social distancing or not. (25% non compliance rate)
    def compliance(self):
        value_compliance = randrange(100) + 1
        if value_compliance > 25:
            is_compliant = True
        else:
            is_compliant = False
        return is_compliant

    # This is a list of all the individuals in the sample population
    PersonList = []

    # This is the count of infected
    infected_counter = 0

    # This is the count of non_compliance with social distancing
    non_compliance_counter = 0

    # This will creates the initial population
    # 5% of the initial population is set to be infected at random
    # 10% of the initial population is set to be non-compliant to social distancing at random
    i = 0
    while i < 100:
        p1 = Person()
        p1.is_healthy = initial_health_stage(self=None)
        p1.is_compliant = compliance(self=None)
        PersonList.append(p1)
        i = i + 1

    for person in PersonList:
        is_healthy = person.is_healthy
        is_compliant = person.is_compliant
        if is_healthy:
            print(colored("This person is healthy.", 'green'),  end=" ")
            if is_compliant:
                print(colored("Compliance: " + str(person.is_compliant), 'green'))
            if not is_compliant:
                print(colored("Compliance: " + str(person.is_compliant), 'red'))
                non_compliance_counter += 1
        elif not is_healthy:
            print(colored("This person is infected.", 'red'), end=" ")
            if is_compliant:
                print(colored("Compliance: " + str(person.is_compliant), 'green'))
            if not is_compliant:
                print(colored("Compliance: " + str(person.is_compliant), 'red'))
                non_compliance_counter += 1
            infected_counter += 1

    print("Number of Infected: " + str(infected_counter))
    print("Number of Non-Compliance: " + str(non_compliance_counter))



