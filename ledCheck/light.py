class Light:
	
    def __init__(self, l):
        self.side = l
        self.grid = [[False for i in range(l)] for i in range(l)]
    
    def on(self, x1, y1, x2, y2):
        a, b, x, y = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        for i in range(a, x+1):
            for j in range(b, y+1):
                if i < self.side and j < self.side:
                    self.grid[i][j] = True
        
    def off(self, x1, y1, x2, y2):
        a, b, x, y = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        for i in range(a, x+1):
            for j in range(b, y+1):
                if i < self.side and j < self.side:
                    self.grid[i][j] = False
    
    def switch(self, x1, y1, x2, y2):
        a, b, x, y = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        for i in range(a, x+1):
            for j in range(b, y+1):
                if i < self.side and j < self.side:
                    self.grid[i][j] = not self.grid[i][j]
    
    def count(self):
        tally = 0
        for i in self.grid:
            for j in i:
                if j:
                    tally += 1
        return tally
