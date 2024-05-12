import tkinter as tk
from tkinter import messagebox
from connect4game import Connect4Game

class Connect4GUI:
    def __init__(self, root, game):
        self.root = root
        self.root.title("Connect 4")
        self.game = game
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(6):
            row = []
            for j in range(7):
                button = tk.Button(self.root, text="", width=4, height=2, command=lambda col=j: self.make_move(col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.status_label.grid(row=6, columnspan=7)

    def make_move(self, column):
        if self.game.currentPlayer is not None:
            if self.game.playTurn(column):
                self.update_board()

    def update_board(self):
        for i in range(6):
            for j in range(7):
                disc = self.game.grid.gridLayout[i][j]
                if disc is None:
                    self.buttons[i][j].config(bg="white")
                else:
                    color = disc.discColor
                    if color == "red":
                        self.buttons[i][j].config(bg="red")
                    elif color == "yellow":
                        self.buttons[i][j].config(bg="yellow")

        if self.game.gameStatus == 'won':
            self.status_label.config(text=f"{self.game.winner.playerName} wins!")
            self.prompt_restart()
        elif self.game.gameStatus == 'draw':
            self.status_label.config(text="It's a draw!")
            self.prompt_restart()

    def prompt_restart(self):
        choice = messagebox.askyesno("Game Over", "Do you want to play again?")
        if choice:
            self.game.restartGame()
            self.status_label.config(text="")
            self.reset_board()
        else:
            self.root.quit()

    def reset_board(self):
        for i in range(6):
            for j in range(7):
                self.buttons[i][j].config(bg="white")
