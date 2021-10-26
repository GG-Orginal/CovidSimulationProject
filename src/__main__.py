from GUI import *
from GUIcontroller import *
from InitialPopulation import *
from Simulation import *
from Person import Person
import time

#startProgram()

def updateStuff():

    updateStatus(Simulation.current_population)
    render_snapshot(Simulation.current_population)
    updatePopStats(0,Person.infected_counter,Person.deceased_counter)
    window.after(1000, updateStuff)
    # time.sleep(1)


updateStuff()

window.mainloop()