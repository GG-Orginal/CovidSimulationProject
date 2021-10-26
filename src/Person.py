class Person:
    # This is the indicator for a healthy person (green).
    is_healthy = None
    # This is the indicator for an infected person (red).
    is_infected = None
    # This is the indicator for a deceased person (black).
    is_deceased = None

    # This is the count of infected
    infected_counter = 0

    # This is the count of deceased
    deceased_counter = 0

    # This is the count of non_compliance with social distancing
    non_compliance_counter = 0

    # This is the constructor
    def __init__(self, is_healthy=True, is_infected=False, is_deceased=False, is_compliant=True, age=25, gender="M"):
        self.is_healthy = is_healthy
        self.is_infected = is_infected
        self.is_deceased = is_deceased
        self.is_compliant = is_compliant
        self.age = age
        self.gender = gender
        self.immune = False
        self.length_of_immunity = 0
        self.length_of_infection = 0

    # def __init__(self):
    #     self

    def changeToInfected(self):
        self.is_infected = True
        self.is_healthy = False
        Person.infected_counter += 1

        # number can be changed later, but set to 10 for now
        self.length_of_infection = 10

    def changeToHealthy(self):
        self.is_healthy = True
        self.is_infected = False
        Person.infected_counter -= 1

        # set the healthy person to immune and change the length of their immunity to 20 days
        self.immune = True
        self.length_of_immunity = 20

    def changeToDeceased(self):
        self.is_deceased = True
        self.is_healthy = False
        self.is_infected = False
        Person.deceased_counter += 1
        Person.infected_counter -= 1


    @staticmethod
    def reset_counters():
        Person.infected_counter = 0
        Person.deceased_counter = 0
