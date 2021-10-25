# Separate from internal logic, this file
# renders the actual user interface
import tkinter as tk

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
percentPopulation = tk.Spinbox(window, from_=0, to=100)
percentPopulation.pack()

def convert():
    spacer2 = tk.Label(window, text="")

percentButton = tk.Button(window, text='Submit', command=convert)
percentButton.pack()
spacer1 = tk.Label(window, text="")
spacer1.pack()
button = tk.Button(
    text="Restart Simulation",
    width=25,
    height=5,
    bg="white",
    fg="black",
)
button.pack()

# Open window
# def startProgram():

    # Actually start the window
    # window.mainloop()
    # print("End of program")


    
