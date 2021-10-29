# Handles the display of backend data onto GUI window
from Person import Person
import tkinter as tk
import GUI
import Simulation
from Simulation import Simulation as sim
import InitialPopulation


####################################################################################
########################### BACKEND TO GUI #########################################
####################################################################################


class PersonPixel:

    def __init__(self, person, x1, y1, size):
        self.person = person
        self.color = 'green' if person.is_healthy else ('black' if person.is_deceased else 'red')
        self.outline = 'white' if person.is_compliant else 'black'
        self.size = size
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + size
        self.y2 = y1 + size

    def drawPerson(self):
        GUI.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color, outline=self.outline)


def render_snapshot(people):
    height = len(people)
    width = len(people[0])

    # Render snapshot of current population
    for i in range(0, height, 1):
        for j in range(0, width, 1):
            # create pixel objects to pass to GUI
            px = PersonPixel(people[i][j], i * 15, j * 15, 15)
            px.drawPerson()


def updatePopStats(new_infections, total_infected, total_deceased):
    GUI.entryDead.delete(0, tk.END)
    GUI.entryDead.insert(0, total_deceased)
    GUI.entryTotalInf.delete(0, tk.END)
    GUI.entryTotalInf.insert(1, total_infected)
    GUI.entryNewInf.delete(0, tk.END)
    GUI.entryNewInf.insert(0, new_infections)


####################################################################################
########################### GUI TO BACKEND #########################################
####################################################################################

def reset_simulation():
    Simulation.reset_population()
    # user_input_initial_infection_rate


def changeValues(val1, val2):
    InitialPopulation.user_input_initial_infection_rate = val1
    InitialPopulation.user_input_non_compliance_rate = val2


def changeRates(infectionLength, immunityDuration, transmissionRate, deathRate):
    Person.default_infection_length = infectionLength
    Person.default_immunity_duration = immunityDuration
    sim.rate_of_transmission = transmissionRate
    sim.death_rate = deathRate
