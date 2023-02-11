class Weighted_Directed:
    def __init__(self,vertices):
        self.vertices = vertices
        self.adj_list = [[] for i in range (vertices)]

    def add_edge(self,v,w,weight):
        self.adj_list[v].append((w,weight))

    def print_graph(self):
        for i,vertices in enumerate(self.adj_list):
            print(f"Adjacency list of vertex {i} -> {vertices}")


if __name__ == "__main__":
    g = Weighted_Directed(6)

    g.add_edge(0,1,6)
    g.add_edge(1,2,7)
    g.add_edge(2,0,5)
    g.add_edge(2,1,4)
    g.add_edge(3,2,10)
    g.add_edge(4,5,3)
    g.add_edge(5,4,1)
    
    g.print_graph()