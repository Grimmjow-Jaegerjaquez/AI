from collections import deque

# define the maximum capacities of the jugs
MAX_5_GALLON_JUG = 5
MAX_3_GALLON_JUG = 3

def water_jug_bfs(target_volume):
    # initialize the starting state with both jugs empty
    start_state = (0, 0)
    # initialize the visited set with the starting state
    visited = {start_state}
    # initialize the queue with the starting state and an empty path
    queue = deque([(start_state, [])])

    while queue:
        # get the current state and path from the queue
        current_state, path = queue.popleft()

        # check if the target volume has been reached
        if current_state[0] == target_volume:
            return path

        # try all possible actions: fill or empty a jug, or pour water from one jug to another
        for action in ['fill_5_gallon', 'fill_3_gallon', 'empty_5_gallon', 'empty_3_gallon', 'pour_5_to_3', 'pour_3_to_5']:
            new_state = apply_action(current_state, action)
            # check if the new state has already been visited
            if new_state not in visited:
                visited.add(new_state)
                new_path = path + [action]
                queue.append((new_state, new_path))

    # if the target volume cannot be reached, return None
    return None

def apply_action(state, action):
    # convert the state tuple to a list to allow modification
    state = list(state)
    if action == 'fill_5_gallon':
        state[0] = MAX_5_GALLON_JUG
    elif action == 'fill_3_gallon':
        state[1] = MAX_3_GALLON_JUG
    elif action == 'empty_5_gallon':
        state[0] = 0
    elif action == 'empty_3_gallon':
        state[1] = 0
    elif action == 'pour_5_to_3':
        diff = min(state[0], MAX_3_GALLON_JUG - state[1])
        state[0] -= diff
        state[1] += diff
    elif action == 'pour_3_to_5':
        diff = min(state[1], MAX_5_GALLON_JUG - state[0])
        state[0] += diff
        state[1] -= diff
    # convert the state list back to a tuple
    return tuple(state)

# run the program to find a solution for 4 gallons in the 5-gallon jug
target_volume = 1
solution = water_jug_bfs(target_volume)
if solution:
    print("Steps to obtain {} gallons in the 5-gallon jug: {}".format(target_volume, solution))
else:
    print("Target volume cannot be obtained.")    
    