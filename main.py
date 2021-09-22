""" Sudoku Solver """
import numpy as np
import requests
from gui import Pygame
import time


# response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
# board = np.array(response.json()['board'])


class Sudoku:
    
    def __init__(self, board):
        self.board = board
        self.not_available = np.argwhere(board==0)
        self.gui = Pygame()

    def is_valid(self, board, row, col, num):
        r, c = row - (row % 3), col - (col % 3)
        if np.count_nonzero(board[row] == num) > 0:
            return False
        elif np.count_nonzero(board[:,col] == num) > 0:
            return False
        elif np.count_nonzero(board[r:r+3, c:c+3] == num) > 0:
            return False
        else:
            return True
    
    def solve(self, board, row=0, col=0):
        if row == 9:
            print(board)
            return True
        elif col == 9:
            return self.solve(board, row+1, 0)
        elif [row,col] not in self.not_available.tolist():
                return self.solve(board, row, col+1)
        else:
            for num in range(1,10):
                if self.is_valid(board, row, col, num): #explore
                    board[row][col] = num #choose
                    time.sleep(0.2)
                    self.gui.display(board, row, col, False)
                    if self.solve(board, row, col+1):
                        return True
                    board[row][col] = 0 #"unchoose"
                    self.gui.display(board, row, col, True)
            return False



board = np.array(
        [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]
         )

def main():
    sudoku = Sudoku(board)
    print("Before\n\n")
    print(board)
    print("\n\nAfter \n\n")
    sudoku.solve(sudoku.board)



main()