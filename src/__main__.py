from GUI import *
from GUIcontroller import *
from InitialPopulation import *
from simulation import *
from Person import Person

ppl = InitialPopulation.createPopulation()

render_snapshot(ppl)

updateStatus(ppl)

startProgram()
