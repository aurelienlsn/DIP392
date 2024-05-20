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
        self.canvas = tk.Canvas(self.root, width=700, height=600, bg='blue')
        self.canvas.grid(row=0, column=0, rowspan=6, columnspan=7)

        self.canvas.bind("<Button-1>", self.click_handler)

        self.status_label = tk.Label(self.root, text="Player 1's turn (Red)", font=("Helvetica", 16))
        self.status_label.grid(row=6, columnspan=7)

        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game, font=("Helvetica", 14))
        self.reset_button.grid(row=7, columnspan=7, pady=10)

        self.draw_board()

    def draw_board(self):
        self.discs = [[None for _ in range(7)] for _ in range(6)]
        for row in range(6):
            for col in range(7):
                x1 = col * 100 + 10
                y1 = row * 100 + 10
                x2 = x1 + 80
                y2 = y1 + 80
                self.discs[row][col] = self.canvas.create_oval(x1, y1, x2, y2, fill="white", outline="blue")

    def click_handler(self, event):
        col = event.x // 100
        self.make_move(col)

    def make_move(self, column):
        if self.game.currentPlayer is not None:
            if self.game.playTurn(column):
                self.update_board()
                self.update_status()

    def update_board(self):
        for i in range(6):
            for j in range(7):
                disc = self.game.grid.gridLayout[i][j]
                if disc is None:
                    self.canvas.itemconfig(self.discs[i][j], fill="white")
                else:
                    color = disc.discColor
                    if color == "red":
                        self.canvas.itemconfig(self.discs[i][j], fill="red")
                    elif color == "yellow":
                        self.canvas.itemconfig(self.discs[i][j], fill="yellow")

        if self.game.gameStatus == 'won':
            self.status_label.config(text=f"{self.game.winner.playerName} wins!")
        elif self.game.gameStatus == 'draw':
            self.status_label.config(text="It's a draw!")

    def update_status(self):
        if self.game.gameStatus == 'playing':
            current_player = "Player 1 (Red)" if self.game.currentPlayer.discColor == "red" else "Player 2 (Yellow)"
            self.status_label.config(text=f"{current_player}'s turn")

    def reset_game(self):
        self.game.restartGame()
        self.status_label.config(text="Player 1's turn (Red)")
        self.reset_board()

    def reset_board(self):
        for i in range(6):
            for j in range(7):
                self.canvas.itemconfig(self.discs[i][j], fill="white")

if __name__ == "__main__":
    root = tk.Tk()
    game = Connect4Game()
    gui = Connect4GUI(root, game)
    root.mainloop()
