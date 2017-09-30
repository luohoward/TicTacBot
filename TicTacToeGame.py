from TicTacToe import TicTacToe
from Minimax import MiniMaxNode
class TicTacToeGame(object):
    def __init__(self):
        self.board = TicTacToe()
        self.turn = 'x'

    def changeTurns(self):
        if self.turn == 'x':
            self.turn = 'o'
        else:
            self.turn = 'x'

    def playGame(self):
        while not self.board.winCondition('x') and not self.board.winCondition('o') and not self.board.boardFull():
            if self.turn == 'x':
                try:
                    self.printBoard()
                    move = raw_input("Enter a move (00 for (0, 0))") 
                    x = int(move[0])
                    y = int(move[1])
                    validMove = self.board.makeMove(x, y, self.turn) 
                    if validMove == "": 
                        self.changeTurns()
                    else:
                        print validMove
                except Exception as e:
                    print str(e)
                    print "Input can not be parsed"
            else:
                node = MiniMaxNode()
                move = node.getBestMove(self.board)
                x = int(move[0])
                y = int(move[1])
                self.board.makeMove(x, y, self.turn) 
                self.changeTurns() 

        if self.board.winCondition('x'):
            print "X wins!"

        elif self.board.winCondition('o'):
            print "O wins!"

        else:
            print "Tie game!"

        self.printBoard() 

    def printBoard(self):
        for row in self.board.board:
            print row

game = TicTacToeGame()
game.playGame()
