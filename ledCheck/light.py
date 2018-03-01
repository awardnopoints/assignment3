class Light:
	
    def __init__(self, l):
        self.side = l
        self.grid = [[0 for i in range(l)] for i in range(l)]
        self.unresolvedCount = l**2
        self.onFinal = 0
    
    def on(self, x1, y1, x2, y2):
        a, b, x, y = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        for i in range(a, x+1):
            for j in range(b, y+1):
                if isinstance(self.grid[i][j], int):
                    self.unresolvedCount -= 1
                    if self.grid[i][j] % 2 == 0:
                        self.onFinal += 1
                    self.grid[i][j] = None
        
    def off(self, x1, y1, x2, y2):
        a, b, x, y = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        for i in range(a, x+1):
            for j in range(b, y+1):
                if isinstance(self.grid[i][j], int):
                    self.unresolvedCount -= 1
                    if self.grid[i][j] % 2 == 1:
                        self.onFinal += 1
                    self.grid[i][j] = None
    
    def switch(self, x1, y1, x2, y2):
        a, b, x, y = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        for i in range(a, x+1):
            for j in range(b, y+1):
                if isinstance(self.grid[i][j], int):
                    self.grid[i][j] += 1
    
    def resolveSwitches(self):
        for i in range(self.side):
            for j in range(self.side):
                if isinstance(self.grid[i][j], int):
                    if self.grid[i][j] % 2 == 1:
                        self.onFinal += 1

