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
percentageLabel = tk.Label(text="Percentage of population complying \n with social distancing recommendations")
percentageLabel.pack()
sliderPopulation = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL)
sliderPopulation.set(23)
sliderPopulation.pack()
tk.Button(window, text='Submit').pack()

PopulationSize = tk.Label(text="Population size")
PopulationSize.place(x=55, y=25)
sliderPopulationSize = tk.Scale(window, from_=3, to=50, orient=HORIZONTAL)
sliderPopulationSize.set(23)
sliderPopulationSize.pack(side=tk.RIGHT)
tk.Button(window, text='Submit').place(x=70, y=90)
sliderPopulationSize.place(x=45, y=50)

PopulationInfected = tk.Label(text="Percentage of initial \n population that is infected")
PopulationInfected.place(x=525, y=20)
sliderPopulationInfected = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL)
sliderPopulationInfected.set(23)
sliderPopulationInfected.pack(side=tk.RIGHT)
tk.Button(window, text='Submit').place(x=560, y=90)
sliderPopulationInfected.place(x=535, y=50)

PopulationDeath = tk.Label(text="Death rate")
PopulationDeath.place(x=65, y=455)
sliderPopulationDeath = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL)
sliderPopulationDeath.set(23)
sliderPopulationDeath.pack(side=tk.RIGHT)
tk.Button(window, text='Submit').place(x=70, y=520)
sliderPopulationDeath.place(x=45, y=480)

PopulationTransmission = tk.Label(text="Rate of \n Transmission")
PopulationTransmission.place(x=545, y=445)
sliderPopulationTransmission = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL)
sliderPopulationTransmission.set(23)
sliderPopulationTransmission.pack(side=tk.RIGHT)
tk.Button(window, text='Submit').place(x=560, y=520)
sliderPopulationTransmission.place(x=535, y=480)

def convert():
    spacer2 = tk.Label(window, text="")


def convert2():
    spacer2 = tk.Label(window, text="")


ImmunityLabel = tk.Label(text="Immunity Rate")
ImmunityLabel.place(x=595, y=225)
ImmunitySpinbox= tk.Spinbox(window, from_=0, to=100)
ImmunitySpinbox.place(x=570, y=260)
percentButton = tk.Button(window, text='Submit', command=convert)
percentButton.place(x=610, y=280)

TimeLabel = tk.Label(text="Infection Time")
TimeLabel.place(x=65, y=225)
TimeSpinbox= tk.Spinbox(window, from_=0, to=100)
TimeSpinbox.place(x=40, y=260)
percent2Button = tk.Button(window, text='Submit', command=convert2)
percent2Button.place(x=75, y=280)

spacer1 = tk.Label(window, text="")
spacer1.pack()

def callbackReset():
    GUIcontroller.reset_simulation()

button = tk.Button(
    text="Restart Simulation",
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


    
