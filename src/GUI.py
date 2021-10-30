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
deceased = tk.Label(text="Total deceased: ")
entryDead = tk.Entry()
totalInfections = tk.Label(text="Total infections: ")
entryTotalInf = tk.Entry()
newInfections = tk.Label(text="New infections: ")
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


percentageLabel = tk.Label(text="Social Distancing Non-Compliance % (Works)")
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


PopulationSize = tk.Label(text="Initial Population Size - (Dimension) (Works)")
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


PopulationInfected = tk.Label(window, text="Initial Infection Rate % (Works)")
PopulationInfected.place(x=525, y=20)
sliderPopulationInfected = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL,
                                    command=getUserInputInitialInfectionRate)
sliderPopulationInfected.set(5)
sliderPopulationInfected.pack(side=tk.RIGHT)
entry1 = tk.Entry(window)
sliderPopulationInfected.place(x=535, y=50)

# --------------------------------------------------------------------------------------
# Death Rate
# --------------------------------------------------------------------------------------

user_input_death_rate = 3


def getUserInputDeathRate(val):
    GUI.user_input_death_rate = val


PopulationDeath = tk.Label(text="Death rate")
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


PopulationTransmission = tk.Label(text="Rate of \n Transmission")
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


def getUserInputImmunityDuration():
    GUI.user_input_immunity_duration = tk.Label(window, text="")


ImmunityLabel = tk.Label(text="Immunity Rate")
ImmunityLabel.place(x=595, y=225)
ImmunitySlider = tk.Scale(window, from_=0, to=100, command=getUserInputImmunityDuration)
ImmunitySlider.place(x=570, y=260)


# --------------------------------------------------------------------------------------
# Infection Time
# --------------------------------------------------------------------------------------
user_input_infection_time = 5


def getUserInputInfectionTime():
    GUI.user_input_infection_time = tk.Label(window, text="")


TimeLabel = tk.Label(text="Infection Time")
TimeLabel.place(x=65, y=225)
TimeSlider = tk.Scale(window, from_=0, to=100, command=getUserInputInfectionTime)
TimeSlider.place(x=40, y=260)
spacer = tk.Label(window, text="")
spacer.pack()


# Restart Simulation - this restarts the simulation based on user inputs
def callbackReset():
    canvas.delete("all")
    GUIcontroller.reset_simulation(GUI.user_input_initial_infection_rate,
                                   GUI.user_input_non_compliance_rate,
                                   GUI.user_input_initial_population_size,
                                   5,
                                   20,
                                   GUI.user_input_transmission_rate,
                                   GUI.user_input_death_rate
                                   )


button = tk.Button(
    text="Start Simulation",
    width=25,
    height=5,
    bg="white",
    fg="black",
    command=callbackReset
)
button.pack()


# Open window
# def startProgram():

# Actually start the window
# window.mainloop()
# print("End of program")


class GUI:
    pass
