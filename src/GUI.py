# Separate from internal logic, this file
# renders the actual user interface
import tkinter as tk
from tkinter import *

def startProgram():

    window = Tk()

    window.configure()

    window.geometry("500x400")


    # Actually start the window
    mainloop()

    # Everything below this will only run when window is closed

    print("End of program")