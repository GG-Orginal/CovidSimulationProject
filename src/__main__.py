from GUI import *
from GUIcontroller import *
from Simulation import *
from Person import Person

user_input_initial_population_size = 20


def updateStuff():
    updateStatus(Simulation.current_population)
    render_snapshot(Simulation.current_population, user_input_initial_population_size)
    updatePopStats(Person.new_infections, Person.infected_counter, Person.deceased_counter)
    window.after(1000, updateStuff)


def start():
    updateStuff()


window.mainloop()


class __main__:
    pass
