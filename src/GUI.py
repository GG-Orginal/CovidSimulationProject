# Separate from internal logic, this file
# renders the actual user interface
import tkinter as tk
import GUIcontroller
from tkinter import HORIZONTAL


# Window set up
from src.Simulation import Simulation

window = tk.Tk()
window.configure()
window.title('Coronavirus Simulation')
window.geometry('750x750')
window.minsize(700, 950)

#------------------------------------------
#Explaination of the Simulation
explain = tk.Label (text = '\n Coronavirus Simulation: ', font = ('Helvetica', 12, 'bold', 'underline'))
explain.pack()


explain2 = tk.Label (text = ' \n This simulation will predict the number \n of covid cases based on your customizations. ', font = ('Helvetica', 10, "italic"))
explain2.pack()

instructions = tk.Label (text = '\n \n Choose from the sliders presented and watch the virus grow. \n')
instructions.pack()

#---------------------------------------------

simulationDays = tk.Label(text="Days: ")
entrySimulationDays = tk.Entry()

deceased = tk.Label(text="Total Deceased: ")
entryDead = tk.Entry()
totalInfections = tk.Label(text="Total Infections: ")
entryTotalInf = tk.Entry()
newInfections = tk.Label(text="New Infections: ")
entryNewInf = tk.Entry()

simulationDays.pack()
entrySimulationDays.pack()

deceased.pack()
entryDead.pack()
totalInfections.pack()
entryTotalInf.pack()
newInfections.pack()
entryNewInf.pack()


#-------------------------------------------------------
#Legend: 
legend = tk.Label (text = '\n Legend: ', font = ('Helvetica', 9, 'bold', 'underline'))
legend_att = tk.Label (text = ' Green = Healthy    Red = Infected     Black = Deceased', font = ('Helvetica', 8, "italic"))

legend.pack()
legend_att.pack()
#---------------------------------------------------------

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
PopulationSize.place(x=5, y=40)
sliderPopulationSize = tk.Scale(window, from_=3, to=50, orient=HORIZONTAL,
                                command=getUserInputInitialPopulationSize)
sliderPopulationSize.set(20)
sliderPopulationSize.pack(side=tk.RIGHT)
sliderPopulationSize.place(x=45, y=75)

# --------------------------------------------------------------------------------------
# Initial Infection Rate
# --------------------------------------------------------------------------------------
user_input_initial_infection_rate = 5


def getUserInputInitialInfectionRate(val):
    GUI.user_input_initial_infection_rate = val



PopulationInfected = tk.Label(window, text="Initial Infection Rate %")
PopulationInfected.place(relx=0.9, rely=0.05, anchor="e")
sliderPopulationInfected = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL,
                                    command=getUserInputInitialInfectionRate)
sliderPopulationInfected.set(5)
entry1 = tk.Entry(window)
sliderPopulationInfected.place(relx=0.9, rely=0.1, anchor="e")

# --------------------------------------------------------------------------------------
# Death Rate
# --------------------------------------------------------------------------------------

user_input_death_rate = 3


def getUserInputDeathRate(val):
    GUI.user_input_death_rate = val


PopulationDeath = tk.Label(text="Death Rate %")
PopulationDeath.place(x=65, y=580)
sliderPopulationDeath = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL,
                                 command=getUserInputDeathRate)
sliderPopulationDeath.set(3)
sliderPopulationDeath.pack(side=tk.RIGHT)
sliderPopulationDeath.place(x=45, y=610)

# --------------------------------------------------------------------------------------
# Transmission Rate
# --------------------------------------------------------------------------------------

user_input_transmission_rate = 75


def getUserInputTransmissionRate(val):
    GUI.user_input_transmission_rate = val


PopulationTransmission = tk.Label(text="Rate of \n Transmission %")
PopulationTransmission.place(relx=0.9, rely=0.62, anchor="e")
sliderPopulationTransmission = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL,
                                        command=getUserInputTransmissionRate)
sliderPopulationTransmission.set(75)
sliderPopulationTransmission.place(relx=0.9, rely=0.67, anchor="e")

# --------------------------------------------------------------------------------------
# Immunity Duration
# --------------------------------------------------------------------------------------
user_input_immunity_duration = 20


def getUserInputImmunityDuration(val):
    GUI.user_input_immunity_duration = val


ImmunityDurationLabel = tk.Label(text="Immunity Duration (Days)")
ImmunityDurationLabel.place(relx=0.95, rely=0.3, anchor="e")
ImmunityDurationSlider = tk.Scale(window, from_=0, to=100, command=getUserInputImmunityDuration)
ImmunityDurationSlider.set(20)
ImmunityDurationSlider.place(relx=0.9, rely=0.4, anchor="e")

# --------------------------------------------------------------------------------------
# Infection Duration
# --------------------------------------------------------------------------------------
user_input_infection_duration = 5


def getUserInputInfectionDuration(val):
    GUI.user_input_infection_duration = val


InfectionDurationLabel = tk.Label(text="Infection Duration (Days)")
InfectionDurationLabel.place(x=20, y=280)
InfectionDurationSlider = tk.Scale(window, from_=0, to=100, command=getUserInputInfectionDuration)
InfectionDurationSlider.set(5)
InfectionDurationSlider.place(x=40, y=325)

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

spacer = tk.Label(window, text="")
spacer.pack()
spacer = tk.Label(window, text="")
spacer.pack()
#--------------------------------------------
#Note

note = tk.Label (text = 'Note: ', font = ('Helvetica', 10, 'bold', 'italic'))
note_Label = tk.Label(text=" Values are only updated upon starting the simulation", font = ('Helvetica', 10, 'italic'))

note.pack()
note_Label.pack()


class GUI:
    pass
