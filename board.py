import sys,pygame
from random import sample   

class Board:
    def __init__(self, height, width, numBombs): 
        self.board = {}
        self.visible = {}
        self.numBombs = numBombs
        self.height,self.width = height,width
        self.populateBoard(height,width)
        self.setBombs(numBombs)
        self.totalFlagged = 0
    
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
            tmpVisited = set()
            for neighbor in neighbors: 
                if self.board[neighbor] == None: 
                    totalBombs += 1
                else:   
                    if neighbor not in visited: 
                        tmp.append(neighbor)
                        tmpVisited.add(neighbor)
            if totalBombs == 0: 
                queue.extend(tmp)
                visited.update(tmpVisited)
            self.board[node] = totalBombs
            self.visible[node] = 1

    def getNeighbors(self, i, j): 
        coords = [(i-1,j-1), (i-1,j), (i-1, j+1), (i,j-1), (i,j), (i,j+1), (i+1,j-1), (i+1, j),  (i+1,j+1)]
        neighbors = []
        for neighbor in coords: 
            a,b = neighbor
            if a > 0 and b > 0 and a < self.height - 1 and b < self.width - 1: 
                if self.visible[neighbor] == 0 or self.visible[neighbor] == 2: 
                    neighbors.append(neighbor)
        return neighbors

    def endGame(self): 
        for i in range(self.height): 
            for j in range(self.width): 
                self.visible[(i,j)] = 1
        
    def flagCell(self, i, j):
        if self.visible[(i,j)] == 2: 
            self.visible[(i,j)] = 0
            self.totalFlagged -= 1
        else: 
            self.visible[(i,j)] = 2
            self.totalFlagged += 1
