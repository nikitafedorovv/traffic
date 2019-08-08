import tkinter as tk
from tkinter import *


class MyGuy:

    def __init__(self):
        self.root = tk.Tk()

        self.redState = Label(text="⬤", fg='red', font=("Courier", 100))
        self.redState.grid(row=0, column=0)

        self.yellowState = Label(text="⬤", fg='yellow', font=("Courier", 100))
        self.yellowState.grid(row=1, column=0)

        self.greenState = Label(text="⬤", fg='green', font=("Courier", 100))
        self.greenState.grid(row=2, column=0)
