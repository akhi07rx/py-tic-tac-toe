# A Test Tic Tac Toe Game built with python and Tkinter.


import tkinter as tk
from tkinter import font


class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TIC TAC TOE")
        self.cells = {}
        self.create_board_display()
        self.create_board_grid()

    def create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)

        self.display = tk.Label(
            master=display_frame, text="READY?", font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(master=grid_frame, text="",
                                   font=font.Font(size=36, weight="bold"), fg="Black", width=3, height=2, highlightbackground="lightblue",)
                self.cells[button] = (row, col)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


def main():
    board = TicTacToeBoard()
    board.mainloop()


if __name__ == "__main__":
    main()
