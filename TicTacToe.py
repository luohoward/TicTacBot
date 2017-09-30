class TicTacToe(object):
    def __init__(self):
        self.board = [[' ' for j in range(3)] for i in range(3)]

    def validMove(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        elif self.board[x][y] == ' ':
            return True
        else:
            return False

    def winCondition(self, move):
        if self.checkColumn(0, move) or self.checkColumn(1, move) or self.checkColumn(2, move):
            return True
        elif self.checkRow(0, move) or self.checkRow(1, move) or self.checkRow(2, move):
            return True
        elif self.checkDiagonals(move):
            return True
        else:
            return False

    def checkColumn(self, colNo, move):
        if self.board[0][colNo] == move and self.board[1][colNo] == move and self.board[2][colNo] == move:
            return True
        else:
            return False


    def checkRow(self, rowNo, move):
        if self.board[rowNo][0] == move and self.board[rowNo][1] == move and self.board[rowNo][2] == move:
            return True
        else:
            return False

    def checkDiagonals(self, move):
        if self.board[0][0] == move and self.board[1][1] == move and self.board[2][2] == move:
            return True
        elif self.board[2][0] == move and self.board[1][1] == move and self.board[0][2] == move:
            return True
        else:
            return False

    def makeMove(self, x, y, move):
        if self.validMove(x, y):
            self.board[x][y] = move
            return ""
        else:
            return "Invalid Move"

    def boardFull(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == ' ':
                    return False
        return True
