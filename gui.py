import pygame
pygame.init()


class Pygame:
    def __init__(self):
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.black = (0,0,0)
        self.green = (0,255,0)
        self.font = pygame.font.SysFont('Arial', 35)
           
    def mainloop(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.time(50)
                    return
    
    def display(self, board, giv_row, giv_col, remove):
        self.window = pygame.display.set_mode((650, 650))
        self.window.fill(self.white)
        pygame.display.set_caption("Sudoku Solver")
        for line in range(10):
            pygame.draw.line(self.window, self.black, start_pos=(100 + 50*line, 100), end_pos=(100 + 50*line, 550), width=1)
            pygame.draw.line(self.window, self.black, start_pos=(100, 100 + 50*line), end_pos=(550, 100 + 50*line), width=1)
            pygame.draw.line(self.window, self.black, start_pos=(100, 100 + 150*line), end_pos=(550, 100 + 150*line), width=3)
            pygame.draw.line(self.window, self.black, start_pos=(100 + 150*line, 100), end_pos=(100 + 150*line, 550), width=3)
    
        for row in range(9):
            for col in range(9):
                if board[row][col] > 0:
                    value = self.font.render(str(board[row][col]), True, self.black)
                    self.window.blit(value, (115+col*50 , 105+row*50))
        if remove:
            col = self.red
        else:
            col = self.green
        pygame.draw.line(self.window, col, start_pos=(100+50*giv_col, 100+50*giv_row), end_pos=(100+50*(giv_col+1), 100+50*giv_row), width=2)
        pygame.draw.line(self.window, col, start_pos=(100+50*giv_col, 100+50*giv_row), end_pos=(100+50*giv_col, 100+50*(giv_row+1)), width=2)
        pygame.draw.line(self.window, col, start_pos=(100+50*(giv_col+1), 100+50*giv_row), end_pos=(100+50*(giv_col+1), 100+50*(giv_row+1)), width=2)
        pygame.draw.line(self.window, col, start_pos=(100+50*giv_col, 100+50*(giv_row+1)), end_pos=(100+50*(giv_col+1), 100+50*(giv_row+1)), width=2)
        
        pygame.display.update()
        
