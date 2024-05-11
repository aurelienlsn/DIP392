import tkinter as tk
from tkinter import messagebox
class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

class Disc:
    def __init__(self, color):
        self.discColor = color

class Player:
    def __init__(self, name, color):
        self.playerName = name
        self.playerColor = color

class Grid:
    def __init__(self, rows, columns):
        self.gridSize = (rows, columns)
        self.gridLayout = [[None for _ in range(columns)] for _ in range(rows)]

    def displayGrid(self):
        for row in self.gridLayout:
            print(' '.join(['O' if disc is None else disc.discColor for disc in row]))

class Connect4Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.currentPlayer = None
        self.winner = None
        self.gameStatus = 'ongoing'
        self.grid = Grid(6, 7)

    def startNewGame(self, player1_name, player2_name):
        self.player1 = Player(player1_name, 'red')
        self.player2 = Player(player2_name, 'yellow')
        self.currentPlayer = self.player1

    def playTurn(self, column):
        for row in reversed(self.grid.gridLayout):
            if row[column] is None:
                row[column] = Disc(self.currentPlayer.playerColor)
                if self.checkForWinner():
                    self.gameStatus = 'won'
                    self.winner = self.currentPlayer
                    return True
                elif self.isBoardFull():
                    self.gameStatus = 'draw'
                    return True
                self.switchPlayer()
                return True
        return False

    def checkForWinner(self):
        for row in range(self.grid.gridSize[0]):
            for col in range(self.grid.gridSize[1] - 3):
                if self.grid.gridLayout[row][col] is not None and \
                    self.grid.gridLayout[row][col].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row][col+1] is not None and \
                    self.grid.gridLayout[row][col+1].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row][col+2] is not None and \
                    self.grid.gridLayout[row][col+2].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row][col+3] is not None and \
                    self.grid.gridLayout[row][col+3].discColor == self.currentPlayer.playerColor:
                    return True

        # Check vertical spaces
        for row in range(self.grid.gridSize[0] - 3):
            for col in range(self.grid.gridSize[1]):
                if self.grid.gridLayout[row][col] is not None and \
                    self.grid.gridLayout[row][col].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row+1][col] is not None and \
                    self.grid.gridLayout[row+1][col].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row+2][col] is not None and \
                    self.grid.gridLayout[row+2][col].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row+3][col] is not None and \
                    self.grid.gridLayout[row+3][col].discColor == self.currentPlayer.playerColor:
                    return True

        # Check / diagonal spaces
        for row in range(self.grid.gridSize[0] - 3):
            for col in range(self.grid.gridSize[1] - 3):
                if self.grid.gridLayout[row][col] is not None and \
                    self.grid.gridLayout[row][col].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row+1][col+1] is not None and \
                    self.grid.gridLayout[row+1][col+1].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row+2][col+2] is not None and \
                    self.grid.gridLayout[row+2][col+2].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row+3][col+3] is not None and \
                    self.grid.gridLayout[row+3][col+3].discColor == self.currentPlayer.playerColor:
                    return True

        # Check \ diagonal spaces
        for row in range(3, self.grid.gridSize[0]):
            for col in range(self.grid.gridSize[1] - 3):
                if self.grid.gridLayout[row][col] is not None and \
                    self.grid.gridLayout[row][col].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row-1][col+1] is not None and \
                    self.grid.gridLayout[row-1][col+1].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row-2][col+2] is not None and \
                    self.grid.gridLayout[row-2][col+2].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row-3][col+3] is not None and \
                    self.grid.gridLayout[row-3][col+3].discColor == self.currentPlayer.playerColor:
                    return True

        return False

    def isBoardFull(self):
        for row in self.grid.gridLayout:
            if None in row:
                return False
        return True

    def restartGame(self):
        self.grid = Grid(6, 7)
        self.currentPlayer = self.player1
        self.winner = None
        self.gameStatus = 'ongoing'

    def switchPlayer(self):
        self.currentPlayer = self.player1 if self.currentPlayer == self.player2 else self.player2

# Tkinter interface
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

# Start the GUI
root = tk.Tk()
game = Connect4Game()
game.startNewGame('Player 1', 'Player 2')
app = Connect4GUI(root, game)
root.mainloop()
