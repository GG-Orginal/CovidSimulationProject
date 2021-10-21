# Handles the display of backend data onto GUI window
import Person
import tkinter as tk
import GUI

class PersonPixel:

    def __init__(self, person: Person, size: int, x1: int, y1: int):
        self.person = person
        self.color = 'green' if person.is_healthy else ('black' if person.is_deceased else 'red')
        self.size = size
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + size
        self.y2 = y1 + size

    def drawPerson(self):
        GUI.canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill=self.color)


def render_snapshot():

    #TODO change to person objects/import from other file
    people = [[1,1,1],[2,2,2],[3,3,3]]

    height = len(people)
    width = len(people[0])

    # Render snapshot of current population
    for i in range(0,height-1,1):
        for j in range(0,width-1,1):

    #create pixel objects to pass to GUI

