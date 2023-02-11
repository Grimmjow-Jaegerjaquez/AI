class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.adj_matrix = [[0 for j in range(self.v)] for i in range(self.v)]
        self.adj_list = {chr(65 + i):[] for i in range(self.v)}

    def add_edge(self,u,v):
        self.adj_list[u].append(v)

    def add_edge_mat(self,u,v):
        u_index = ord(u) - 65
        v_index = ord(v) - 65
        self.adj_matrix[u_index][v_index] = 1
        self.adj_matrix[v_index][u_index] = 1

    def print_graph(self):
        for i in self.adj_list:
            print(i,"->","->".join([str(j) for j in self.adj_list[i]]))

    def print_matrix(self):
        for i in range(self.v):
            for j in range(self.v):
                print(self.adj_matrix[i][j],end = " ")
            print()

g = Graph(5)

g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('A','E')
g.add_edge('B','A')
g.add_edge('B','C')
g.add_edge('B','D')
g.add_edge('C','A')
g.add_edge('C','B')
g.add_edge('C','D')
g.add_edge('C','E')
g.add_edge('D','C')
g.add_edge('D','B')
g.add_edge('E','A')
g.add_edge('E','C')

g.add_edge_mat('A','B')
g.add_edge_mat('A','C')
g.add_edge_mat('A','E')
g.add_edge_mat('B','A')
g.add_edge_mat('B','C')
g.add_edge_mat('B','D')
g.add_edge_mat('C','A')
g.add_edge_mat('C','B')
g.add_edge_mat('C','D')
g.add_edge_mat('C','E')
g.add_edge_mat('D','C')
g.add_edge_mat('D','B')
g.add_edge_mat('E','A')
g.add_edge_mat('E','C')

g.print_matrix()
g.print_graph()