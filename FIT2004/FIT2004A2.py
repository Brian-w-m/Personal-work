# preferences = [[1], [0, 1], [0, 1], [0], [1], [0, 1], [1, 0], [1, 0], [0], [0]]
# licences = [1, 0, 5, 8, 3, 2, 4, 6, 7]

# Output = [[8, 3, 1, 2, 9], [0, 4, 5, 6, 7]]

# preferences = [[0], [1], [0,1], [0, 1], [1, 0], [1], [1, 0], [0, 1], [1]]
# licences = [1, 4, 0, 5, 8]

# Output = [[0, 4, 3, 2], [1, 5, 6, 7, 8]]

preferences = [[1], [0, 1], [0], [1, 0], [0], [0]]
licences = [0, 1, 2, 4]

# Output = [[2, 4, 5], [0, 1, 3]]


class Edge:
    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0
    def __str__(self):
        return f"({self.u}, {self.v}, {self.capacity})"


def dfs(u, t, bottleneck):
    if u == t:
        return bottleneck

    visited[u] = True

    for edge in graph[u]:
        v, residual = edge.v, edge.capacity - edge.flow
        if residual > 0 and not visited[v]:
            augment = dfs(v, t, min(bottleneck, residual))
            if augment > 0:
                edge.flow += augment
                edge.reverse.flow -= augment
                return augment
    return 0


def max_flow(G, s, t):
    global visited
    flow = 0

    while True:
        visited = [False] * len(G)
        augment = dfs(s, t, float('inf'))
        if augment > 0:
            flow += augment
        else:
            break

    return flow

# number of people
ppl_num = len(preferences)

# find number of locations
max_loclen = 0
for preference in preferences:
    if len(preference) > max_loclen:
        max_loclen = len(preference)

# defining source and sink
source = 0
sink = ppl_num + 2*max_loclen + 2

# Create a graph as an adjacency list
n = ppl_num + 2*max_loclen + 3  # Number of nodes
graph = [[] for _ in range(n)]

edges = []
for index, preference in enumerate(preferences):
    edges.append(Edge(0, index+1, 1))
    for location in preference:
        if index in licences:
            edges.append(Edge(index+1, 1 + ppl_num + 2*location,1))
        edges.append(Edge(index+1, 1 + ppl_num + 2*location + 1,1))
for loc in range(0,2*max_loclen,2):
    edges.append(Edge(loc + 1 + ppl_num, sink, 2))
for loc in range(1,2*max_loclen,2):
    edges.append(Edge(loc + 1 + ppl_num, sink-1, 3))
edges.append(Edge(sink-1, sink, ppl_num-2-2))

for edge in edges:
    reverse_edge = Edge(edge.v, edge.u, 0)
    edge.reverse = reverse_edge
    reverse_edge.reverse = edge
    graph[edge.u].append(edge)
    graph[edge.v].append(reverse_edge)

max_flow_value = max_flow(graph, source, sink)
print("Maximum Flow:", max_flow_value)

for i in graph:
    for j in i:
        print(j.flow, j)

