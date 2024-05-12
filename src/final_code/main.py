import tkinter as tk
from connect4game import Connect4Game
from connect4gui import Connect4GUI

try:
    # Start the GUI
    root = tk.Tk()
    game = Connect4Game()
    game.startNewGame('Player 1', 'Player 2')
    app = Connect4GUI(root, game)
    root.mainloop()
except ValueError as ve:
    print("ValueError:", ve)
except TypeError as te:
    print("TypeError:", te)
except Exception as e:
    print("An error occurred:", e)
