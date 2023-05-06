import heapq

# Define the goal state
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

# Define the heuristic function
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(state[i][j]-1, 3)
                distance += abs(x-i) + abs(y-j)
    return distance

# Define the function to get the neighbors of a state
def get_neighbors(state):
    neighbors = []
    row, col = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    for i, j in ((row-1, col), (row, col-1), (row, col+1), (row+1, col)):
        if 0 <= i < 3 and 0 <= j < 3:
            neighbor_state = [row[:] for row in state]
            neighbor_state[row][col], neighbor_state[i][j] = neighbor_state[i][j], neighbor_state[row][col]
            neighbors.append(neighbor_state)
    return neighbors

# Define the A* search algorithm
def search(initial_state):
    # Initialize the priority queue
    pq = []
    heapq.heappush(pq, (heuristic(initial_state), initial_state, 0, []))
    # Initialize the visited set
    visited = set()
    # Perform the A* search
    while pq:
        _, state, cost, path = heapq.heappop(pq)
        if state == goal_state:
            return (cost, path+[state])
        visited.add(tuple(map(tuple, state)))
        for neighbor_state in get_neighbors(state):
            if tuple(map(tuple, neighbor_state)) not in visited:
                neighbor_cost = cost + 1
                neighbor_path = path + [state]
                heapq.heappush(pq, (neighbor_cost+heuristic(neighbor_state), neighbor_state, neighbor_cost, neighbor_path))
    return None

initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]

# Call the search function to find the solution
solution = search(initial_state)

# Print the solution
if solution:
    cost, path = solution
    print(f"Cost: {cost}")
    for state in path:
        print(state)
else:
    print("No solution found.")