import sys
import copy
from TicTacToe import TicTacToe
from random import *

class MiniMaxNode(object):
    def minimax(self, board, isMax):
        if board.winCondition('o'):
            return 10
        elif board.winCondition('x'):
            return -10
        elif board.boardFull():
            return 0
        else:
            if isMax:
                maxValue = -sys.maxint

                for i in range(3):
                    for j in range(3):
                        if board.validMove(i, j):
                            board.makeMove(i, j, 'o')
                            maxValue = max(maxValue, self.minimax(board, not isMax))
                            board.board[i][j] = ' '
                return maxValue

            else:
                minValue = sys.maxint

                for i in range(3):
                    for j in range(3):
                        if board.validMove(i, j):
                            board.makeMove(i, j, 'x')
                            minValue = min(minValue, self.minimax(board, not isMax))
                            board.board[i][j] = ' '
                return minValue

    def getBestMove(self, board):
        if board.boardFull():
            return "No more moves"

        bestMove = -sys.maxint 
        bestMoveX = -1
        bestMoveY = -1
        for i in range(3):
            for j in range(3):
                if board.validMove(i, j):
                    board.makeMove(i, j, 'o')
                    moveVal = self.minimax(board, False)
                    board.board[i][j] = ' '

                    if moveVal > bestMove:
                        bestMove = moveVal
                        bestMoveX = i
                        bestMoveY = j

                    if moveVal == bestMove:
                        rand = random() 
                        if rand <= 0.5:
                            bestMoveX = i
                            bestMoveY = j

        return str(bestMoveX) + str(bestMoveY)
        
