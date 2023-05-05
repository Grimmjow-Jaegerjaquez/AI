def dfs(state, visited):
    """
    Recursive function to explore all possible states using Depth First Search
    """
    if state in visited:
        return False
    visited.add(state)
    if state[0] == 4 and state[1] == 4:
        return True
    for i in range(3):
        for j in range(3):
            if i != j:
                # Pour water from jug i to jug j
                new_state = list(state)
                amount = min(new_state[i], jug_capacity[j] - new_state[j])
                new_state[i] -= amount
                new_state[j] += amount
                if dfs(tuple(new_state), visited):
                    print(new_state)
                    return True
    return False

# Define the initial state and the capacities of the jugs
initial_state = (8, 0, 0)
jug_capacity = (8, 5, 3)

# Call the dfs function to solve the problem
visited = set()
dfs(initial_state, visited)