from GUI import *
from GUIcontroller import *
from InitialPopulation import *
from Simulation import *
from Person import Person
import time

user_input_initial_population_size = 20


def updateStuff():
    updateStatus(Simulation.current_population)
    # render_snapshot(Simulation.current_population)
    render_snapshot(Simulation.current_population, user_input_initial_population_size)
    updatePopStats(0, Person.infected_counter, Person.deceased_counter)
    window.after(1000, updateStuff)
    # time.sleep(1)



def start():
    updateStuff()


window.mainloop()


class __main__:
    pass
