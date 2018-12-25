import sys,pygame
from random import sample   

class Board:
    def __init__(self, height, width, numBombs): 
        self.board = {}
        self.visible = {}
        self.height,self.width = height,width
        self.populateBoard(height,width)
        self.setBombs(numBombs)
    
    def populateBoard(self, height, width):
        for i in range(height): 
            for j in range(width): 
                self.board[(i,j)] = 0
                self.visible[(i,j)] = 0

    def setBombs(self, numBombs): 
        allKeys = self.board.keys()
        self.bombs = sample(allKeys, numBombs)
        for bomb in self.bombs: 
            self.board[bomb] = None

    def checkBomb(self, i, j):
        if self.board[(i,j)] == None: 
            return True 
        return False 

    def updateBoard(self, i, j): 
        queue = [(i,j)]
        visited = set()
        while queue: 
            node = queue.pop(0)
            neighbors = self.getNeighbors(node[0],node[1])
            totalBombs = 0
            tmp = []
            for neighbor in neighbors: 
                if self.board[neighbor] == None: 
                    totalBombs += 1
                else:   
                    if neighbor not in visited: 
                        tmp.append(neighbor)
                        visited.add(neighbor)
            if totalBombs == 0: 
                queue.extend(tmp)
            self.board[node] = totalBombs
            self.visible[node] = 1

    def getNeighbors(self, i, j): 
        coords = [(i-1,j-1), (i-1,j), (i,j-1), (i+1,j), (i,j+1), (i-1,j+1), (i+1, j-1),  (i+1,j+1)]
        neighbors = []
        for neighbor in coords: 
            a,b = neighbor
            if a > 0 and b > 0 and a < self.height - 1 and b < self.width - 1: 
                if self.visible[neighbor] == 0: 
                    neighbors.append(neighbor)
        return neighbors

    def endGame(self): 
        for i in range(self.height): 
            for j in range(self.width): 
                self.visible[(i,j)] = 1

board = Board(80,90,15)    

