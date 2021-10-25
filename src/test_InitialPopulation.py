import unittest

from InitialPopulation import createPopulation


class TestInitialPopulation(unittest.TestCase):
    def test_length(self):
        initial_population = createPopulation()
        self.assertEqual(len(initial_population), 20)
        self.assertEqual(len(initial_population[10]), 20)





