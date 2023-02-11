class Unweighted_Directed:

    def __init__(self,vertices):
        self.vertices = vertices
        self.adj_list = [[] for i in range (vertices)]

    def add_edge(self,v,w):
        self.adj_list[v].append(w)

    def print_Graph(self):
        for i,vertices in enumerate(self.adj_list):
            print(f"Adjacency list of vertex {i} -> {vertices}")

if __name__ == "__main__":
    g = Unweighted_Directed(6)

    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(2,1)
    g.add_edge(3,2)
    g.add_edge(4,5)
    g.add_edge(5,4) 

    g.print_Graph()
