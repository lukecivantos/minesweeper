import sys

import pygame
from pygame.locals import *

from random import sample   

from board import Board


class Minesweeper: 
    def __init__(self): 

        runGame = self.getBoardSize()
        
        if runGame:
            self.boardWidth = 15
            self.boardHeight = 25

            self.cellWidth = 20
            self.cellHeight = 20

            self.numBombs = 40
            self.margin = 5

            self.pixelHeight  = (self.boardHeight*(self.cellHeight + self.margin)) + self.margin
            self.pixelWidth = (self.boardWidth*(self.cellWidth + self.margin)) + self.margin

            self.won = False
            self.lost = False

            self.runGame()

    def getBoardSize(self):
        return True


        running = True 
        while running: 
            for event in pygame.event.get(): 
                if event.type == KEYDOWN: 
                    if event.key == K_ESCAPE: 
                        running = False
                elif event.type == MOUSEBUTTONUP: 
                    pass
                elif event.type == QUIT: 
                    running = False
        return False

    def runGame(self): 
        self.displayBoard()

        RIGHTCLICK = 3
        LEFTCLICK = 1
        running = True

        


        while running: 
            for event in pygame.event.get(): 
                if event.type == KEYDOWN: 
                    if event.key == K_ESCAPE: 
                        running = False
                elif event.type == MOUSEBUTTONUP:
                    if event.button == RIGHTCLICK: 
                        pos = pygame.mouse.get_pos()
                        pos = (((pos[1]*self.boardHeight)/self.pixelHeight), ((pos[0]*self.boardWidth)/self.pixelWidth)) 
                        if self.board.visible[pos] != 1: 
                            self.flagCell(pos)
                    elif event.button == LEFTCLICK:    
                        if self.lost == True: 
                            self.lost = False
                            self.board = Board(self.boardHeight, 
                                               self.boardWidth, 
                                               self.numBombs) 
                            self.updateBoard()
                            continue

                        pos = pygame.mouse.get_pos()
                        pos = (((pos[1]*self.boardHeight)/self.pixelHeight), ((pos[0]*self.boardWidth)/self.pixelWidth)) 
                        if self.board.visible[pos] == 0: 
                            self.clickCell(pos)
                            if self.won: 
                                print("You Won!")
                elif event.type == QUIT: 
                    running = False

    def displayBoard(self): 
        pygame.init()

        self.screen = pygame.display.set_mode((self.pixelWidth, self.pixelHeight))
        pygame.display.set_caption("Minesweeper")

        self.board = Board(self.boardHeight, self.boardWidth, self.numBombs) 
        self.updateBoard()

    def updateBoard(self):
        # Define some colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)

        self.screen.fill(BLACK)

        # Draw the grid
        for row in range(self.boardHeight):
            for column in range(self.boardWidth):
                color = WHITE
                if self.board.visible[(row,column)] == 1: 
                    if self.board.board[(row,column)] == None:
                        color = RED
                    else: 
                        color = GREEN
                curRect = pygame.draw.rect(self.screen,
                                color,
                                [(self.margin + self.cellWidth) * column + self.margin,
                                (self.margin + self.cellHeight) * row + self.margin,
                                self.cellWidth,
                                self.cellHeight])

                num = self.board.board[(row,column)]
                if num != None and num != 0: 
                    font = pygame.font.Font(pygame.font.get_default_font(), 20)
                    text = font.render(str(num), 1, (10, 10, 10))
                    #textpos = text.get_rect()
                    self.screen.blit(text, curRect)
                
                if self.board.visible[(row,column)] == 2: 
                    font = pygame.font.Font(pygame.font.get_default_font(), 20)
                    text = font.render("F", 1, (10, 10, 10))
                    #textpos = text.get_rect()
                    self.screen.blit(text, curRect) 

        pygame.display.flip()

    def clickCell(self, pos):
        i,j = pos
        if self.board.checkBomb(i,j): 
            self.board.endGame()
            self.updateBoard()
            self.lost = True
        else: 
            self.board.updateBoard(i,j)
            self.updateBoard()
            totalVisible = self.board.getNumVisible()
            if totalVisible == ((self.boardWidth * self.boardHeight) - self.numBombs): 
                self.won = True

    def flagCell(self,pos):
        i,j = pos
        self.board.flagCell(i,j)
        self.updateBoard()
        



Minesweeper()