


class Game:

    EMPTY = " "
    p1 = "X"
    p2 = "O"

    def __init__(self):
        self.__board = [[Game.EMPTY for _ in range(3)] for _ in range(3)]
        self.__player = Game.p1

    def __repr__(self):
        return "Current Board:"

    def play(self,row,col):
        row -= 1 # 0-basing
        col -= 1
        self.__board[row][col] = self.__player
        if self.__player == Game.p1:
            self.__player = Game.p2
        else:
            self.__player = Game.p1
    
    @property
    def winner(self):
        return None

if __name__ == "__main__":
    pass
