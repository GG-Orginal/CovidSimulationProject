# Separate from internal logic, this file
# renders the actual user interface
import tkinter as tk
import GUIcontroller
from tkinter import HORIZONTAL

# Window set up
window = tk.Tk()
window.configure()
window.title('Coronavirus Simulation')
window.geometry('750x750')
deceased = tk.Label(text="Total Deceased: ")
entryDead = tk.Entry()
totalInfections = tk.Label(text="Total Infections: ")
entryTotalInf = tk.Entry()
newInfections = tk.Label(text="New Infections: ")
entryNewInf = tk.Entry()
deceased.pack()
entryDead.pack()
totalInfections.pack()
entryTotalInf.pack()
newInfections.pack()
entryNewInf.pack()
canvas = tk.Canvas(window, width=300, height=300, bg="White")
canvas.place(relx=0.5, rely=0.5, anchor="center")
canvas.pack(pady=10)

# --------------------------------------------------------------------------------------
# Non-Compliance Rate
# --------------------------------------------------------------------------------------
user_input_non_compliance_rate = 25


def getUserInputNonComplianceRate(val):
    GUI.user_input_non_compliance_rate = val


percentageLabel = tk.Label(text="Social Distancing Non-Compliance %")
percentageLabel.pack()
sliderPopulation = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL,
                            command=getUserInputNonComplianceRate)
sliderPopulation.set(25)
sliderPopulation.pack()

# --------------------------------------------------------------------------------------
# Initial Population Size
# --------------------------------------------------------------------------------------
user_input_initial_population_size = 20


def getUserInputInitialPopulationSize(val):
    GUI.user_input_initial_population_size = val


PopulationSize = tk.Label(text="Initial Population Size - (Dimension)")
PopulationSize.place(x=5, y=25)
sliderPopulationSize = tk.Scale(window, from_=3, to=50, orient=HORIZONTAL,
                                command=getUserInputInitialPopulationSize)
sliderPopulationSize.set(20)
sliderPopulationSize.pack(side=tk.RIGHT)
sliderPopulationSize.place(x=45, y=50)

# --------------------------------------------------------------------------------------
# Initial Infection Rate
# --------------------------------------------------------------------------------------
user_input_initial_infection_rate = 5


def getUserInputInitialInfectionRate(val):
    GUI.user_input_initial_infection_rate = val


PopulationInfected = tk.Label(window, text="Initial Infection Rate %")
PopulationInfected.place(x=560, y=25)
sliderPopulationInfected = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL,
                                    command=getUserInputInitialInfectionRate)
sliderPopulationInfected.set(5)
sliderPopulationInfected.pack(side=tk.RIGHT)
entry1 = tk.Entry(window)
sliderPopulationInfected.place(x=580, y=50)

# --------------------------------------------------------------------------------------
# Death Rate
# --------------------------------------------------------------------------------------

user_input_death_rate = 3


def getUserInputDeathRate(val):
    GUI.user_input_death_rate = val


PopulationDeath = tk.Label(text="Death Rate %")
PopulationDeath.place(x=65, y=455)
sliderPopulationDeath = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL,
                                 command=getUserInputDeathRate)
sliderPopulationDeath.set(3)
sliderPopulationDeath.pack(side=tk.RIGHT)
sliderPopulationDeath.place(x=45, y=480)

# --------------------------------------------------------------------------------------
# Transmission Rate
# --------------------------------------------------------------------------------------

user_input_transmission_rate = 75


def getUserInputTransmissionRate(val):
    GUI.user_input_transmission_rate = val


PopulationTransmission = tk.Label(text="Rate of \n Transmission %")
PopulationTransmission.place(x=545, y=445)
sliderPopulationTransmission = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL,
                                        command=getUserInputTransmissionRate)
sliderPopulationTransmission.set(75)
sliderPopulationTransmission.pack(side=tk.RIGHT)
sliderPopulationTransmission.place(x=535, y=480)

# --------------------------------------------------------------------------------------
# Immunity Duration
# --------------------------------------------------------------------------------------
user_input_immunity_duration = 20


def getUserInputImmunityDuration(val):
    GUI.user_input_immunity_duration = val


ImmunityDurationLabel = tk.Label(text="Immunity Duration (Days)")
ImmunityDurationLabel.place(x=550, y=225)
ImmunityDurationSlider = tk.Scale(window, from_=0, to=100, command=getUserInputImmunityDuration)
ImmunityDurationSlider.set(20)
ImmunityDurationSlider.place(x=570, y=260)

note_Label = tk.Label(text = "Note: Values are only updated upon starting the simulation")
note_Label.place(x = 213, y = 640)

# --------------------------------------------------------------------------------------
# Infection Duration
# --------------------------------------------------------------------------------------
user_input_infection_duration = 5


def getUserInputInfectionDuration(val):
    GUI.user_input_infection_duration = val


InfectionDurationLabel = tk.Label(text="Infection Duration (Days)")
InfectionDurationLabel.place(x=20, y=225)
InfectionDurationSlider = tk.Scale(window, from_=0, to=100, command=getUserInputInfectionDuration)
InfectionDurationSlider.set(5)
InfectionDurationSlider.place(x=40, y=260)

spacer = tk.Label(window, text="")
spacer.pack()




# Start Simulation - this starts the simulation based on user inputs
def callbackReset():
    canvas.delete("all")
    GUIcontroller.reset_simulation(GUI.user_input_initial_infection_rate,
                                   GUI.user_input_non_compliance_rate,
                                   GUI.user_input_initial_population_size,
                                   GUI.user_input_infection_duration,
                                   GUI.user_input_immunity_duration,
                                   GUI.user_input_transmission_rate,
                                   GUI.user_input_death_rate,
                                   100)


button = tk.Button(
    text="Start Simulation",
    width=25,
    height=5,
    bg="white",
    fg="black",
    command=callbackReset
)
button.pack()




class GUI:
    pass
