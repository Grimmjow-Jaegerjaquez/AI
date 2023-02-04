from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_Edge(self, u, v):
        self.graph[u].append(v)


g = Graph(4)
g.add_Edge(1,[[2,1],[3,1]])
g.add_Edge(2,[3,3])
g.add_Edge(3,[4,4])
g.add_Edge(4,[1,5])

for i in range(1,g.V+1):
    print("Adjacency list of vertex {}: {}".format(i, g.graph[i]))