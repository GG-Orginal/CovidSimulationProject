


class Person:
    # # This is the indicator for a healthy person (green).
    # is_healthy = None
    # # This is the indicator for an infected person (red).
    # is_infected = None
    # # This is the indicator for a deceased person (black).
    # is_deceased = None

     # This is the count of infected
    infected_counter = 0

    # This is the count of deceased
    deceased_counter = 0

    # This is the count of non_compliance with social distancing
    non_compliance_counter = 0

    # This is the indicator for social distancing compliance.
    is_compliant = None
    age = None
    gender = None

    # This is the constructor
    def Person(self, is_healthy, is_infected, is_deceased, is_compliant, age, gender):
        self.is_healthy = is_healthy
        self.is_infected = is_infected
        self.is_deceased = is_deceased
        self.is_compliant = is_compliant
        self.age = age
        self.gender = gender

    def __init__(self):
        self

    def changeToInfected(self):
        self.is_infected = True
        infected_counter += 1

    def changeToHealthy(self):
        self.is_healthy = True
        infected_counter -= 1

    def changeToDeceased(self):
        self.is_deceased = True
        deceased_counter += 1
        infected_counter -= 1
