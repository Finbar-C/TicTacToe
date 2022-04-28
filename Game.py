


class Game:

    EMPTY = " "
    p1 = "X"
    p2 = "O"

    def __init__(self):
        self.__board = [[Game.EMPTY for _ in range(3)] for _ in range(3)]
        self.__player = Game.p1

    def __repr__(self):
        result = "  " + " ".join(str(i+1) for i in range(3))
        for row in range(3):
            result += f"\n{row+1} " + "|".join(self.__board[row])
            if row != 2:
                dashes = "-" * 5
                result += f"\n  {dashes}"
        result += f"\n\n{self.__player} turn to play"
        return result

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
        for p in (Game.p1, Game.p2):
            for row in range(3):
                if all(self.__board[row][col] == p for col in range(3)):
                    return p
            for col in range(3):
                if all(self.__board[row][col] == p for row in range(3)):
                    return p
            if all(self.__board[i][i] == p for i in range(3)):
                return p
            if all(self.__board[2-i][i] == p for i in range(3)):
                return p
            
        return None


if __name__ == "__main__":
    pass
