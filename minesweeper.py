import sys

import pygame
from pygame import init
from pygame.locals import *

from random import sample   

from board import Board


class Minesweeper: 
    def __init__(self): 
        self.width = 630
        self.height = 405
        self.margin = 5
        self.size = (self.width, self.height)

        self.runGame()
      
    def runGame(self): 
        self.displayBoard()

        running = True
        while running: 
            for event in pygame.event.get(): 
                if event.type == KEYDOWN: 
                    if event.key == K_ESCAPE: 
                        running = False
                elif event.type == MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    pos = (((pos[1]*16)/405), ((pos[0]*25)/630)) 
                    if self.board.visible[pos] != 1: 
                        self.clickCell(pos)
                elif event.type == QUIT: 
                    running = False

    def displayBoard(self): 
        init()

        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Minesweeper")

        self.board = Board(16,25,100) 
        self.updateBoard()

    def updateBoard(self):
        # Define some colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
 
        # This sets the WIDTH and HEIGHT of each grid location
        WIDTH = 20
        HEIGHT = 20
        
        # This sets the margin between each cell
        MARGIN = 5
        
        self.screen.fill(BLACK)

        # Draw the grid
        for row in range(16):
            for column in range(25):
                color = WHITE
                if self.board.visible[(row,column)] == 1: 
                    if self.board.board[(row,column)] == None:
                        color = RED
                    else: 
                        color = GREEN

                curRect = pygame.draw.rect(self.screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])

                num = self.board.board[(row,column)]
                if num != None and num != 0: 
                    font = pygame.font.Font(pygame.font.get_default_font(), 12)
                    text = font.render("1", True, (0xff, 0xff, 0xff))
                    text_rect = text.get_rect()
                    text_rect.center = curRect.center

        pygame.display.flip()

    def clickCell(self, pos):
        i,j = pos
        if self.board.checkBomb(i,j): 
            self.board.endGame()
            self.updateBoard()
        else: 
            self.board.updateBoard(i,j)
            self.updateBoard()

        



Minesweeper()