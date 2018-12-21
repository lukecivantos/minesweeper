import sys,pygame
from random import sample   

class Board:
    def __init__(self, height, width, numBombs): 
        self.board = {}
        self.visible = {}
        self.populateBoard(height,width)
        self.setBombs(numBombs)
    
    def populateBoard(self, height, width):
        for i in range(height): 
            for j in range(width): 
                self.board[(i,j)] = 0
                self.visible = 0

    def setBombs(self, numBombs): 
        allKeys = self.board.keys()
        self.bombs = sample(allKeys, numBombs)
        for bomb in self.bombs: 
            self.board[bomb] = None
        print(self.bombs)

    def checkBomb(self, i, j):
        if self.board[(i,j)] == None: 
            return True 
        return False 

    
board = Board(80,90,15)    

