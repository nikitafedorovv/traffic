import tkinter as tk
from tkinter import *


class MyGuy:

    def __init__(self):
        self.root = tk.Tk()

        # Label(text="⬤", fg='red').grid(row=0, column=0)
        # Label(text="⬤", fg='yellow').grid(row=1, column=0)
        # Label(text="⬤", fg='green').grid(row=2, column=0)

        self.greenState = Label(text="⬤", fg='green')
        self.greenState.grid(row=0, column=0)

        self.yellowState = Label(text="⬤", fg='yellow')
        self.yellowState.grid(row=1, column=0)

        self.redState = Label(text="⬤", fg='red')
        self.redState.grid(row=2, column=0)
