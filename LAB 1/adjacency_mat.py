def adjacency_matrix(edges, vertices):
    mat = [[0 for j in range(vertices)] for i in range(vertices)]
    for (start,end,weight) in edges:
        mat[start][end] = weight
    return mat

vertices = 4
edges = [[0,1,1],[0,2,1],[1,2,3],[2,3,4],[3,0,5]]

print(adjacency_matrix(edges,vertices))