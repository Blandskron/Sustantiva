class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        print(f"Arista añadida: {u} -> {v}")

    def bfs(self, start):
        visited = set()
        queue = []

        queue.append(start)
        visited.add(start)

        print("Inicio de BFS:")
        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for neighbour in self.graph.get(s, []):
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbour in self.graph.get(v, []):
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, start):
        visited = set()
        print("Inicio de DFS:")
        self.dfs_util(start, visited)

# Ejemplo de uso
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("\nRecorrido BFS (empezando desde el vértice 2):")
g.bfs(2)

print("\nRecorrido DFS (empezando desde el vértice 2):")
g.dfs(2)

