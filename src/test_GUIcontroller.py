import unittest

from GUIcontroller import *
import GUIcontroller
from Person import Person


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
        sample = Person(user_input_initial_infection_rate = 10)
        

        






