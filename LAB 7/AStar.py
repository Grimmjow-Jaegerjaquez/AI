from heapq import *

class AStar():
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.h = heuristics

    def search(self, start, goal):
        openList = []
        heappush(openList, (0, (start, [start], 0)))
        min_cost = float('inf')
        min_path = []
        while openList:
            f, (node, path, length) = heappop(openList)
			
            if node in goal:
                return path, length

            for neighbour, dist in self.graph[node]:
                if neighbour not in path:
                    heappush(openList, (length+dist+self.h[neighbour], (neighbour, path+[neighbour], length+dist)))



