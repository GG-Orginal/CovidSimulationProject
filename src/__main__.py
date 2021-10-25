from GUI import *
from GUIcontroller import *
from InitialPopulation import *
from simulation import *
from Person import Person
import time

ppl = createPopulation()

#startProgram()

while True:

    updateStatus(ppl)

    render_snapshot(ppl)

    window.update()

    time.sleep(1)