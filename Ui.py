from abc import ABC, abstractmethod
from Game import Game, GameError
from tkinter import *

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = Tk()
        root.title("Tic Tac Toe")
        frame = Frame(root)
        frame.pack()
        self.__root = root

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()
    
    def __get_input(self):
        while True:
            try: #type
                row = int(input("enter row: "))
                col = int(input("enter column: "))
                if 1 <= row <= 3 and 1 <= col <= 3: #range
                    break
                else:
                    print("Invalid input, try again")
            except ValueError:
                print("Invalid input, try again")
        return row, col

    def run(self):
        while self.__game.winner == None:
            print(self.__game)
            row, col = self.__get_input()
            try:
                self.__game.play(row,col)
            except GameError as e:
                print(e)
        print(self.__game)
        if self.__game.winner == Game.DRAW:
            print("Draw")
        else:
            print(f"The winner is {self.__game.winner}")

