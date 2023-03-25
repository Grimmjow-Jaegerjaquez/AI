from queue import PriorityQueue

graph = {
    'A': {'B' : 6, 'F' : 3},
    'B': {'C' : 3, 'D' : 2},
    'C': {'D' : 1, 'E' : 5},
    'D': {'E' : 8},
    'E': {'J' : 5, 'I' : 5},
    'F': {'G' : 1, 'H' : 7},
    'G': {'I' : 3},
    'H': {'I' : 2},
    'I': {'J' : 3},   
}

heuristic = {
            'A': 10,
            'B': 8,
            'C': 5,
            'D': 7,
            'E': 3,
            'F': 6,
            'G': 5,
            'H': 3,
            'I': 1, 
            'J': 0
}

def greedy_best_first_search(graph, start, goal):
    queue = PriorityQueue()
    queue.put((0, start))

    visited = {start: None}

    while not queue.empty():
        current = queue.get()[1]

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.put((heuristic[neighbor], neighbor))
                visited[neighbor] = current

    return None

start = 'A'
goal = 'J'
path = greedy_best_first_search(graph, start, goal)

if path is not None:
    print(' -> '.join(path))
    total_cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
    print(f'Total cost: {total_cost}')
else:
    print(f'There is no path from {start} to {goal}.')

