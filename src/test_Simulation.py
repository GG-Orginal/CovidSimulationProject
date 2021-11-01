import unittest

from src.Person import Person
from src.Simulation import initiatePopulation
from src.Simulation import transmit
from src.Simulation import updateStatus


class TestSimulation(unittest.TestCase):
     def test_transmitBothCompliantNotTransmission(self):
        p1 = Person(is_healthy=True, is_infected=False, is_deceased=False, is_compliant=True, is_vaccinated=False, age=25, gender="M")
        p2 = Person(is_healthy=True, is_infected=False, is_deceased=False, is_compliant=True, is_vaccinated= False, age=25, gender="F")
        transmit_population = transmit(p1, p2)
        self.assertEqual(None, transmit_population)

    def test_transmitBothHealthyNotTransmission(self):
        p1 = Person(is_healthy=True, is_infected=False, is_deceased=False, is_compliant=True, is_vaccinated= False, age=26, gender="M")
        p2 = Person(is_healthy=True, is_infected=False, is_deceased=False, is_compliant=True, is_vaccinated= False, age=25, gender="F")
        transmit_population = transmit(p1, p2)
        self.assertEqual(None, transmit_population)

    def test_transmitBothInfectedNotTransmission(self):
        p1 = Person(is_healthy=False, is_infected=True, is_deceased=False, is_compliant=False, is_vaccinated= False, age=25, gender="M")
        p2 = Person(is_healthy=False, is_infected=True, is_deceased=False, is_compliant=False, is_vaccinated= False, age=25, gender="F")
        transmit_population = transmit(p1, p2)
        self.assertEqual(None, transmit_population)

    def test_transmitBothVaccinatedNotTransmission(self):
        p1 = Person(is_healthy=False, is_infected=False, is_deceased=False, is_compliant=False, is_vaccinated=True, age=25, gender="M")
        p2 = Person(is_healthy=False, is_infected=False, is_deceased=False, is_compliant=False, is_vaccinated=True, age=25, gender="F")
        transmit_population = transmit(p1, p2)
        self.assertEqual(None, transmit_population)

    def test_update(self):
        population_array = [[Person() for j in range(20)] for i in range(20)]
        for i in range(len(population_array)):
            for j in range(len(population_array[i])):
                p1 = Person()
                p1.is_healthy = True
                p1.is_infected = not False
                p1.is_compliant = True
                population_array[i][j] = p1
                update_status = updateStatus(population_array)
        self.assertEqual(population_array, update_status)

