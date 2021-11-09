import unittest

from InitialPopulation import createPopulation


class TestInitialPopulation(unittest.TestCase):
    def test_length(self):
        initial_population = createPopulation()
        self.assertEqual(20, len(initial_population))
        self.assertEqual(20, len(initial_population[0]))

    def test_persons_age(self):
        initial_population = createPopulation()
        for i in range(len(initial_population)):
            for j in range(len(initial_population[i])):
                age = initial_population[i][j].age
                self.assertEqual(25, age)

    def test_persons_gender(self):
        initial_population = createPopulation()
        for i in range(len(initial_population)):
            for j in range(len(initial_population[i])):
                gender = initial_population[i][j].gender
                self.assertEqual("M", gender)

    def test_infections(self):
        infected_count = 0
        initial_population = createPopulation()
        for i in range(len(initial_population)):
            for j in range(len(initial_population[i])):
                if initial_population[i][j].is_infected:
                    infected_count += 1
        self.assertGreater(infected_count, 0)
        self.assertLess(infected_count, 401)

    def test_non_compliance(self):
        non_compliance = 0
        initial_population = createPopulation()
        for i in range(len(initial_population)):
            for j in range(len(initial_population[i])):
                if not initial_population[i][j].is_compliant:
                    non_compliance += 1
        self.assertGreater(non_compliance, 0)
        self.assertLess(non_compliance, 401)

