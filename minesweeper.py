import sys,pygame
from random import sample   

from board import Board


class Minesweeper: 
    def __init__(self): 
        pygame.init()
        self.width = 400
        self.height = 300
        self.size = (self.width, self.height)
        self.black = 0, 0, 0
        self.displayGame()
      
    def generateGame(self): 
        self.board = Board(80,90,15)    

    def displayGame(self): 
        screen = pygame.display.set_mode(self.size)
        screen.fill(self.black)
        block_size = 3
        color = 14,12,1
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                pygame.draw.rect(screen, color, rect)
        while True: 
            pass
Minesweeper()