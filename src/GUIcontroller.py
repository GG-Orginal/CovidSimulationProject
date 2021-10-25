# Handles the display of backend data onto GUI window
from Person import Person
import tkinter as tk
import GUI
import numpy as np

class PersonPixel:

    def __init__(self, person: Person, x1: int, y1: int, size: int):
        self.person = person
        self.color = 'green' if person.is_healthy else ('black' if person.is_deceased else 'red')
        self.outline = 'white' if person.is_compliant else 'black'
        self.size = size
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + size
        self.y2 = y1 + size

    def drawPerson(self):
        GUI.canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill=self.color,outline=self.outline)


def render_snapshot(people):

    height = len(people)
    width = len(people[0])

    # Render snapshot of current population
    for i in range(0,height,1):
        for j in range(0,width,1):

            #create pixel objects to pass to GUI
            px = PersonPixel(people[i][j],i*15,j*15,15)

            px.drawPerson()

