# An adjacency list represents a graph as a dictionary where each key is 
# a node, and its corresponding value is a list of adjacent nodes (or neighbors).

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
        
    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                self.graph[neighbor].remove(vertex)
            del self.graph[vertex]
        
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph[vertex2] and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)
            
    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        result = []
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([v for v in self.graph[vertex] if v not in visited])
        return result
    
    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        result = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                stack.extend([v for v in self.graph[vertex] if v not in visited])
        return result
        
    def __str__(self):
        return str(self.graph)