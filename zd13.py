from collections import deque

class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]
        self.adj_list = [[] for _ in range(vertices)]
    
    def add_edge_matrix(self, u, v, weight=1):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_matrix[u][v] = weight
            if not self.directed:
                self.adj_matrix[v][u] = weight
    
    def add_edge_list(self, u, v, weight=1):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_list[u].append((v, weight))
            if not self.directed:
                self.adj_list[v].append((u, weight))
    
    def bfs_matrix(self, start):
        visited = [False] * self.vertices
        queue = deque([start])
        visited[start] = True
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in range(self.vertices):
                if self.adj_matrix[vertex][neighbor] != 0 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return result
    
    def bfs_list(self, start):
        visited = [False] * self.vertices
        queue = deque([start])
        visited[start] = True
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor, _ in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return result
    
    def dfs_matrix(self, start):
        visited = [False] * self.vertices
        result = []
        
        def dfs_util(v):
            visited[v] = True
            result.append(v)
            
            for neighbor in range(self.vertices):
                if self.adj_matrix[v][neighbor] != 0 and not visited[neighbor]:
                    dfs_util(neighbor)
        
        dfs_util(start)
        return result
    
    def dfs_list(self, start):
        visited = [False] * self.vertices
        result = []
        
        def dfs_util(v):
            visited[v] = True
            result.append(v)
            
            for neighbor, _ in self.adj_list[v]:
                if not visited[neighbor]:
                    dfs_util(neighbor)
        
        dfs_util(start)
        return result
    
    def shortest_path_unweighted(self, start, end):
        if start == end:
            return [start], 0
        
        visited = [False] * self.vertices
        parent = [-1] * self.vertices
        queue = deque([start])
        visited[start] = True
        
        while queue:
            vertex = queue.popleft()
            
            if vertex == end:
                path = []
                while vertex != -1:
                    path.append(vertex)
                    vertex = parent[vertex]
                return path[::-1], len(path) - 1
            
            for neighbor, _ in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = vertex
                    queue.append(neighbor)
        
        return [], -1
    
    def print_matrix(self):
        print("Матрица смежности:")
        print("   " + " ".join(f"{i:2}" for i in range(self.vertices)))
        for i in range(self.vertices):
            print(f"{i:2} " + " ".join(f"{self.adj_matrix[i][j]:2}" for j in range(self.vertices)))
    
    def print_list(self):
        print("Список смежности:")
        for i in range(self.vertices):
            neighbors = ", ".join(f"{v}({w})" for v, w in self.adj_list[i])
            print(f"{i}: [{neighbors}]")
