from player import Player
from grid import Grid
from disc import Disc

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
                elif self.isBoardFull():  # Vérifie si la grille est pleine
                    self.gameStatus = 'draw'  # Marque le jeu comme un match nul
                    return True
                else:
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
        for row in range(self.grid.gridSize[0] - 1, 2, -1):
            for col in range(self.grid.gridSize[1]):
                if self.grid.gridLayout[row][col] is not None and \
                    self.grid.gridLayout[row][col].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row-1][col] is not None and \
                    self.grid.gridLayout[row-1][col].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row-2][col] is not None and \
                    self.grid.gridLayout[row-2][col].discColor == self.currentPlayer.playerColor and \
                    self.grid.gridLayout[row-3][col] is not None and \
                    self.grid.gridLayout[row-3][col].discColor == self.currentPlayer.playerColor:
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