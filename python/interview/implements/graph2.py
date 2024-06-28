# An adjacency matrix represents a graph as a 2D list (or array) where the element
# at row i and column j is 1 if there is an edge between vertices i and j, and 0 otherwise.


class GraphMatrix:
    def __init__(self, num_vertices):
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]
        self.num_vertices = num_vertices
        
    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1][vertex2] = 1
        self.graph[vertex2][vertex1] = 1
        
    def remove_edge(self, vertex1, vertex2):
        self.graph[vertex1][vertex2] = 0
        self.graph[vertex2][vertex1] = 0
        
    def bfs(self, start_vertex):
        visited = [False] * self.num_vertices
        queue = [start_vertex]
        result = []
        
        while queue:
            vertex = queue.pop(0)
            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)
                queue.extend([i for i in range(self.num_vertices) if self.graph[vertex][i] and not visited[i]])
                
        return result
    
    
    def dfs(self, start_vertex):
        visited = [False] * self.num_vertices
        stack = [start_vertex]
        result = []
        
        
        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)
                stack.extend([i for i in range(self.num_vertices) if self.graph[vertex][i] and not visited[i]])
        return result
    
    
    def __str__(self):
        return '\n'.join([''.join([str(cell) for cell in row]) for row in self.graph])