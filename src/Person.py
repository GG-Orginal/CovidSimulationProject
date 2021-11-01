class Person:
    # This is the count of infected
    infected_counter = 0

    # This is the count of deceased
    deceased_counter = 0

    # This is the count of non_compliance with social distancing
    non_compliance_counter = 0

    # This is the time period an infected person will stay infected before becoming healthy (if they did not die)
    default_infection_length = 5

    # This is the time period an infected person will remain healthy after become healthy
    default_immunity_duration = 20

    # This is the constructor
    def __init__(self, is_healthy=True, is_infected=False, is_deceased=False, is_compliant=True, is_vaccinated=True, age=25, gender="M"):
        self.is_healthy = is_healthy
        self.is_infected = is_infected
        self.is_deceased = is_deceased
        self.is_compliant = is_compliant
        self.is_vaccinated = is_vaccinated
        self.age = age
        self.gender = gender
        self.immune = False
        self.length_of_immunity = Person.default_immunity_duration
        self.length_of_infection = Person.default_infection_length

    def changeToInfected(self):
        self.is_infected = True
        self.is_healthy = False
        Person.infected_counter += 1

        # number can be changed later, but set to 10 for now
        self.length_of_infection = Person.default_infection_length

    def changeToHealthy(self):
        self.is_healthy = True
        self.is_infected = False
        Person.infected_counter -= 1

        # set the healthy person to immune and change the length of their immunity to 20 days
        self.immune = True
        self.length_of_immunity = Person.default_immunity_duration

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
