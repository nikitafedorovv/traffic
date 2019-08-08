import tkinter as tk
from tkinter import *

LIGHT_ON_STR = '⚫'
LIGHT_OFF_STR = '⚪'


class MyGuy:

    def __init__(self):
        self.root = tk.Tk()

        self.redState = Label(text=LIGHT_ON_STR, fg='red', font=("Arial", 100))
        self.redState.grid(row=0, column=0)

        self.yellowState = Label(text=LIGHT_ON_STR, fg='yellow', font=("Arial", 100))
        self.yellowState.grid(row=1, column=0)

        self.greenState = Label(text=LIGHT_ON_STR, fg='green', font=("Arial", 100))
        self.greenState.grid(row=2, column=0)
