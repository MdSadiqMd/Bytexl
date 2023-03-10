from collections import defaultdict as dd
class Graph:
    def __init__(self):
        self.graph = dd(list)

    def addEdgetoGraph(self, x, y):
        self.graph[x].append(y)

    def BFSearch(self, n):
        visited_vertices = (len(self.graph)) * [False]
        queue = []
        visited_vertices[n] = True
        queue.append(n)
        while queue:
            n = queue.pop(0)
            print(n, end="")
            for v in self.graph[n]:
                if visited_vertices[v] == False:
                    queue.append(v)
                    visited_vertices[v] = True
Graph = Graph()
Graph.addEdgetoGraph(0, 1)
Graph.addEdgetoGraph(1, 1)
Graph.addEdgetoGraph(2, 2)
Graph.addEdgetoGraph(3, 1)
print("the breadth First search is")
Graph.BFSearch(3)
