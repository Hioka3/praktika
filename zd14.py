class Islands:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.visited = [[False] * self.cols for _ in range(self.rows)]
    
    def _is_valid(self, row, col):
        return (0 <= row < self.rows and 
                0 <= col < self.cols and 
                self.grid[row][col] == 1 and 
                not self.visited[row][col])
    
    def _dfs(self, row, col):
        stack = [(row, col)]
        self.visited[row][col] = True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                     (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        while stack:
            r, c = stack.pop()
            
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if self._is_valid(new_row, new_col):
                    self.visited[new_row][new_col] = True
                    stack.append((new_row, new_col))
    
    def _bfs(self, row, col):
        from collections import deque
        queue = deque([(row, col)])
        self.visited[row][col] = True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                     (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if self._is_valid(new_row, new_col):
                    self.visited[new_row][new_col] = True
                    queue.append((new_row, new_col))
    
    def count_islands_dfs(self):
        if self.rows == 0 or self.cols == 0:
            return 0
        
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        island_count = 0
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 1 and not self.visited[i][j]:
                    self._dfs(i, j)
                    island_count += 1
        
        return island_count
    
    def count_islands_bfs(self):
        if self.rows == 0 or self.cols == 0:
            return 0
        
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        island_count = 0
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 1 and not self.visited[i][j]:
                    self._bfs(i, j)
                    island_count += 1
        
        return island_count
    
    def get_island_sizes(self):
        if self.rows == 0 or self.cols == 0:
            return []
        
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        island_sizes = []
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 1 and not self.visited[i][j]:
                    size = self._measure_island(i, j)
                    island_sizes.append(size)
        
        return island_sizes
    
    def _measure_island(self, row, col):
        stack = [(row, col)]
        self.visited[row][col] = True
        size = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while stack:
            r, c = stack.pop()
            size += 1
            
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if self._is_valid(new_row, new_col):
                    self.visited[new_row][new_col] = True
                    stack.append((new_row, new_col))
        
        return size
    
    def print_grid(self):
        print("Сетка островов:")
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
