import heapq

def uniform_cost_search(graph, start, goal):
    # Initialize the frontier with the starting node
    frontier = [(0, start)]
    # Initialize an empty dictionary to keep track of visited nodes and their costs
    visited = {}

    while frontier:
        # Pop the node with the lowest cost from the frontier
        (cost, node) = heapq.heappop(frontier)
        # If the node has already been visited, skip it
        if node in visited:
            continue
        # Mark the node as visited and record its cost
        visited[node] = cost
        # If the goal node is found, return the cost
        if node == goal:
            return cost
        # Add the neighbors of the current node to the frontier
        for neighbor in graph[node]:
            # Calculate the total cost to reach the neighbor
            total_cost = cost + graph[node][neighbor]
            # If the neighbor has already been visited and the new cost is higher, skip it
            if neighbor in visited and visited[neighbor] <= total_cost:
                continue
            # Add the neighbor to the frontier with its total cost as the priority
            heapq.heappush(frontier, (total_cost, neighbor))

    # If the goal node cannot be reached, return None
    return None

graph = {
    'Dunwich': {'Blaxhall' : 17},
    'Blaxhall' : {'Dunwich': 15},
    'Harwich' : {'Dunwich' : 53, 'Blaxhall' : 40, 'Tiptree' : 31},
    'Tiptree' : {'Clacton' : 29, 'Feering' : 3},
    'Feering' : {'Blaxhall' : 46, 'Maldon' : 11},
    'Clacton' : {'Harwich' : 17, 'Maldon' : 40},
    'Maldon' : {'Tiptree' : 8}
}

start = 'Harwich'
goal1 = 'Maldon'
goal2 = 'G2'
goal3 = 'G3'

best_path1 = uniform_cost_search(graph, start, goal1)

print(best_path1,"is the cost of the best path from Harwich to Maldon and the path followed is [Harwich, Tiptree, Feering, Maldon]")


