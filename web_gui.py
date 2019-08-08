import tkinter as tk
from tkinter import *

LIGHT_STR = '⚫'
CIRCLE_SIZE = 100
FONT = 'Arial'


class MyGuy:

    def __init__(self):
        self.root = tk.Tk()

        self.redState = Label(text=LIGHT_STR, fg='red', font=(FONT, CIRCLE_SIZE))
        self.redState.grid(row=0, column=0)

        self.yellowState = Label(text=LIGHT_STR, fg='yellow', font=(FONT, CIRCLE_SIZE))
        self.yellowState.grid(row=1, column=0)

        self.greenState = Label(text=LIGHT_STR, fg='green', font=(FONT, CIRCLE_SIZE))
        self.greenState.grid(row=2, column=0)
