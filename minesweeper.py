import sys

import pygame
from pygame import init
from pygame.locals import *

from random import sample   

from board import Board


class Minesweeper: 
    def __init__(self): 
        self.width = 400
        self.height = 600
        self.size = (self.width, self.height)

        self.runGame()
      
    def generateGame(self): 
        self.board = Board(80,90,15)    

    def runGame(self): 
        init()

        #populate screen
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((0,0,0))

        running = True
        while running: 
            for event in pygame.event.get(): 
                if event.type == KEYDOWN: 
                    if event.key == K_ESCAPE: 
                        running = False
                elif event.type == QUIT: 
                    running = False
            
                


Minesweeper()