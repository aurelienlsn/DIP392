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
            print(' '.join(['O' if disc is None else 'X' if disc.discColor == 'red' else 'Y' for disc in row]))

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
                    print(f"{self.currentPlayer.playerName} wins!")
                    return True
                elif self.isBoardFull():
                    self.gameStatus = 'draw'
                    print("It's a draw!")
                    return True
                self.switchPlayer()
                return True
        return False

    def checkForWinner(self):
        # check horizontal spaces
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

        # check vertical spaces
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

        # check / diagonal spaces
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

        # check \ diagonal spaces
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

    def displayGrid(self):
        self.grid.displayGrid()

# Text-based interface
while True:
    game = Connect4Game()
    game.startNewGame('Player 1', 'Player 2')

    while game.gameStatus == 'ongoing':
        game.displayGrid()
        column = int(input(f"{game.currentPlayer.playerName}'s turn. Choose a column: "))
        if not game.playTurn(column):
            print("Invalid move. Try again.")
            continue
        if game.checkForWinner():
            game.winner = game.currentPlayer  # Set the winner to the current player
            print(f"{game.winner.playerName} wins!")
            break
        if game.isBoardFull():
            print("It's a draw!")
            break

    game.displayGrid()

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break