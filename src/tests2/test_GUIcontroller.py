import unittest

from GUIcontroller import *
import GUIcontroller


class TestGUIController(unittest.TestCase):

    def test_PersonPixelSize(self):
        p = Person(is_healthy=True, is_infected=False, is_deceased=False, is_compliant=True, age=25, gender="M")

        px = GUIcontroller.PersonPixel(person=p, x1=5, y1=10, size=20)

        self.assertEqual(px.x2, 25)
        self.assertEqual(px.y2, 30)

    def test_PersonPixelColor(self):
        p = Person(is_healthy=True, is_infected=False, is_deceased=False, is_compliant=True, age=25, gender="M")

        px = GUIcontroller.PersonPixel(person=p, x1=5, y1=10, size=20)

        self.assertEqual(px.color, 'green')
        self.assertEqual(px.outline, 'white')

        p = Person(is_healthy=False, is_infected=True, is_deceased=False, is_compliant=True, age=25, gender="M")

        px = GUIcontroller.PersonPixel(person=p, x1=5, y1=10, size=20)

        self.assertEqual(px.color, 'red')
        self.assertEqual(px.outline, 'white')

        p = Person(is_healthy=False, is_infected=False, is_deceased=True, is_compliant=True, age=25, gender="M")

        px = GUIcontroller.PersonPixel(person=p, x1=5, y1=10, size=20)

        self.assertEqual(px.color, 'black')
        self.assertEqual(px.outline, 'white')

        p = Person(is_healthy=True, is_infected=False, is_deceased=False, is_compliant=False, age=25, gender="M")

        px = GUIcontroller.PersonPixel(person=p, x1=5, y1=10, size=20)

        self.assertEqual(px.outline, 'black')

    def test_callBackReset(self):
        pass
        # sample = Person(user_input_initial_infection_rate=10)

    def test_user_inputs(self):
        test_value_initial_infection_rate = 50
        test_value_non_compliance_rate = 250
        test_value_initial_population_size = 200

        GUIcontroller.reset_simulation(test_value_initial_infection_rate, test_value_non_compliance_rate,
                                       test_value_initial_population_size, 5, 5, 5, 5, 50)

        self.assertEqual(test_value_initial_infection_rate, InitialPopulation.user_input_initial_infection_rate)
        self.assertEqual(test_value_non_compliance_rate, InitialPopulation.user_input_non_compliance_rate)

        self.assertEqual(test_value_initial_population_size, InitialPopulation.user_input_initial_population_size)
        self.assertEqual(test_value_initial_population_size, Simulation.user_input_initial_population_size)
        self.assertEqual(test_value_initial_population_size, GUI.user_input_initial_population_size)

        self.assertEqual(Person.default_infection_length, 5)
        self.assertEqual(Person.default_immunity_duration, 5)
        self.assertEqual(Simulation.rate_of_transmission, 5)
        self.assertEqual(Simulation.death_rate, 5)

