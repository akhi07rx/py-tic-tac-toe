# A Test Tic Tac Toe Game built with python and Tkinter.


import tkinter as tk
from tkinter import font


class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TIC TAC TOE")
        self.cells = {}

    def create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame, text="READY?", font=font.Font(size=28, weight="bold"),)
        self.display.pack()
