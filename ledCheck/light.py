class Light:
	
    def __init__(self, l):
        self.side = l
        self.grid = [[False for i in range(l)] for i in range(l)]
    
    def on(self, x1, y1, x2, y2):
        a, b, x, y = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        x = min(x, self.side-1)
        y = min(y, self.side-1)
        i = max(a, 0)
        while i <= x:
            j = max(b, 0)
            while j <= y:
                self.grid[i][j] = True
                j += 1
            i += 1
        
    def off(self, x1, y1, x2, y2):
        a, b, x, y = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        x = min(x, self.side-1)
        y = min(y, self.side-1)
        i = max(a, 0)
        while i <= x:
            j = max(b, 0)
            while j <= y:
                self.grid[i][j] = False
                j += 1
            i += 1
    
    def switch(self, x1, y1, x2, y2):
        a, b, x, y = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        x = min(x, self.side-1)
        y = min(y, self.side-1)
        i = max(a, 0)
        while i <= x:
            j = max(b, 0)
            while j <= y:
                self.grid[i][j] = not self.grid[i][j]
                j += 1
            i += 1
    
    def count(self):
        tally = 0
        for i in self.grid:
            for j in i:
                if j:
                    tally += 1
        return tally
