import unittest

from src.Person import Person

class TestPerson(unittest.TestCase):

    Person.sample_infected_counter = 0

    #Test to see if the change to infected method changes the infection to true & sets healthy to false & increments infected counter
    def test_changeToInfected(self):
        sample_infect = Person()
        expected = True
        sample_infect.changeToInfected()
        actual = sample_infect.is_infected
        self.assertEqual(expected, actual)

    def test_changeToInfectedTwo(self):
        sample_healthy = Person()
        expected = False
        sample_healthy.changeToInfected()
        actual = sample_healthy.is_healthy
        self.assertEqual(expected, actual)

    #Should be incremented
    def test_changeToInfectedThree(self):
        sample_infected_counter = Person()
        expected = 1
        sample_infected_counter.changeToInfected()
        actual = sample_infected_counter.infected_counter
        self.assertEqual(expected, actual)


    #Test to see if the change to healthy method changes healthy to true & sets infected to false & decrements infected counter
    def test_changeToHealthy(self):
        sample_healthy = Person()
        expected = True
        sample_healthy.changeToHealthy()
        actual = sample_healthy.is_healthy
        self.assertEqual(expected, actual)

    def test_changeToHealthyTwo(self):
        sample_infected = Person()
        expected = False
        sample_infected.changeToHealthy()
        actual = sample_infected.is_infected
        self.assertEqual(expected, actual)

    #Should be decremented
    def test_changeToHealthyThree(self):
        sample_infected_counter = Person()
        expected = 0
        sample_infected_counter.changeToInfected()
        actual = sample_infected_counter.infected_counter
        self.assertEqual(expected, actual)


    #Test to see if the change to deceased method changes deceased to true & sets healthy to false & increments the deceased counter & decrements the infected counter
    def test_changeToDeceased(self):
        sample_deceased = Person()
        expected = True
        sample_deceased.changeToDeceased()
        actual = sample_deceased.is_deceased
        self.assertEqual(expected, actual)

    def test_changeToDeceasedTwo(self):
        sample_healthy = Person()
        expected = False
        sample_healthy.changeToDeceased()
        actual = sample_healthy.is_healthy
        self.assertEqual(expected, actual)

    #Should be decremented
    def test_changeToDeceasedThree(self):
        sample_infected_counter = Person()
        expected = 1
        sample_infected_counter.changeToInfected()
        actual = sample_infected_counter.infected_counter
        self.assertEqual(expected, actual)
    

    #Should be incremented 
    def test_changeToDeceasedFour(self):
        sample_deceased_counter = Person()
        expected = 0
        sample_deceased_counter.changeToInfected()
        actual = sample_deceased_counter.infected_counter
        self.assertEqual(expected, actual)
