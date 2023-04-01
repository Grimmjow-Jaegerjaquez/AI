import heapq

def ucs(graph, start, goal):
    frontier = [(0, start)]
    visited = {}

    while frontier:
        (cost, node) = heapq.heappop(frontier)
        if node in visited:
            continue
        visited[node] = cost
        if node == goal:
            return cost
        for neighbor in graph[node]:
            total_cost = cost + graph[node][neighbor]
            if neighbor in visited and visited[neighbor] <= total_cost:
                continue
            heapq.heappush(frontier, (total_cost, neighbor))

    return None

graph = {
    'S' : {1 : 2, 3 : 5},

}