import random

def TSP(graph, start):
    # initialize the path with the starting node
    path = [start]
    # choose a random neighbor node
    current_node = random.choice(list(graph[start].keys()))
    # add the chosen neighbor to the path
    path.append(current_node)
    # set the total cost of the path
    total_cost = graph[start][current_node]

    # iterate until all nodes have been visited
    while len(path) < len(graph):
        # get the neighbors of the current node
        neighbors = list(graph[current_node].keys())
        # remove the nodes that have already been visited
        unvisited_neighbors = [n for n in neighbors if n not in path]
        if not unvisited_neighbors:
            # if all neighbors have been visited, return to the starting node
            current_node = start
        else:
            # choose the neighbor with the lowest cost
            costs = [graph[current_node][n] for n in unvisited_neighbors]
            min_cost_index = costs.index(min(costs))
            current_node = unvisited_neighbors[min_cost_index]
        # add the chosen neighbor to the path and update the total cost
        path.append(current_node)
        total_cost += graph[path[-2]][current_node]

    # add the cost of returning to the starting node
    total_cost += graph[path[-1]][start]

    return total_cost, path

graph = {
    'A' : {'B' : 2, 'C' : 3, 'D' : 1},
    'B' : {'A' : 2, 'C' : 4, 'D' : 2},
    'C' : {'A' : 3, 'B' : 4, 'D' : 3},
    'D' : {'A' : 1, 'B' : 2, 'C' : 3}
}

start = 'A'
print(TSP(graph, start))