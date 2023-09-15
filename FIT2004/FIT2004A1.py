def restaurantFinder(d, site_list):
    max_profits = [0] * len(site_list)
    
    # Need first loop since we cannot assume d < len(site_list)
    for i in range(0,min(d+1, len(site_list))):
        if site_list[i] > max_profits[i-1]:
            max_profits[i] = site_list[i]
        else:
            max_profits[i] = max_profits[i-1]

    for j in range(d+1, len(site_list)):
        if max_profits[j-1] > max_profits[j-d-1] + site_list[j]:
            max_profits[j] = max_profits[j-1]
        else:
            max_profits[j] = max_profits[j-d-1] + site_list[j]
    
    # Getting site lists from max_profits list
    rests = []  
    k = len(site_list)-1
    while k>=0:
        if k == 0 and max_profits[0]>0:
            rests.append(1)
        if max_profits[k]> max_profits[k-1]:
            rests.append(k+1)
            k = k-d-1
        else:
            k = k-1

    return max_profits[-1], rests[::-1]



# print(restaurantFinder(1, [50, 10, 12, 65, 40, 95, 100, 12, 20, 30])) #252 [1,4,6,8,10]
# print(restaurantFinder(2, [50, 10, 12, 65, 40, 95, 100, 12, 20, 30])) #245 [1,4,7,10]
# print(restaurantFinder(3, [50, 10, 12, 65, 40, 95, 100, 12, 20, 30])) #175 [1,6,10]
# print(restaurantFinder(7, [50, 10, 12, 65, 40, 95, 100, 12, 20, 30])) #100 [7]
# print(restaurantFinder(0, [50, 10, 12, 65, 40, 95, 100, 12, 20, 30])) #434 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(restaurantFinder(7, [1]))

import heapq as heap

class graph:
    def __init__(self, paths, keys):
        currentMaxNode = 0
        for path in paths:
            currentMaxNode = max(path[0], path[1], currentMaxNode)
        self.maxNode = currentMaxNode

        self.adjacencyList = []
        for _ in range(2*(self.maxNode + 1)):
            self.adjacencyList.append([])

        for path in paths:
            self.adjacencyList[path[0]].append([path[1], path[2]])
            self.adjacencyList[path[0]+self.maxNode+1].append([path[1]+self.maxNode+1, path[2]])

        for key in keys:
            self.adjacencyList[key[0]].append([key[0]+self.maxNode+1, key[1]])

    def climb(self, start, exits):
        dist = []

        for _ in range(2*(self.maxNode + 1)):
            dist.append(float('inf'))
            
        dist[start] = 0

        queue = [(0,start)]

        while queue:
            dist_u, u = heap.heappop(queue)
            if dist_u > dist[u]:
                continue

            for v, weight in self.adjacencyList[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heap.heappush(queue, (dist[v], v))
        return dist




grraph = graph([(0, 1, 4), (1, 2, 2), (2, 3, 3), (3, 4, 1), (1, 5, 2), (5, 6, 5), (6, 3, 2), (6, 4, 3), (1, 7, 4), (7, 8, 2), (8, 7, 2), (7, 3, 2), (8, 0, 11), (4, 3, 1), (4, 8, 10)], [(5, 10), (6, 1), (7, 5), (0, 3), (8, 4)])
print(grraph.adjacencyList)
start = 1
exits = [7, 2, 4]
print(grraph.climb(start, exits))