import tkinter as tk
from tkinter import *


class MyGuy:

    def __init__(self):
        self.root = tk.Tk()

        Label(text="⬤", fg='red').grid(row=0, column=0)
        Label(text="⬤", fg='yellow').grid(row=1, column=0)
        Label(text="⬤", fg='green').grid(row=2, column=0)

        self.greenState = Label(self.root, text="0")
        self.greenState.grid(row=2, column=1)

        self.yellowState = Label(self.root, text="1")
        self.yellowState.grid(row=1, column=1)

        self.redState = Label(self.root, text="1")
        self.redState.grid(row=0, column=1)
