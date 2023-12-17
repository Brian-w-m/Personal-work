### DO NOT CHANGE THIS FUNCTION
def load_dictionary(filename):
    infile = open(filename)
    word, frequency = "", 0
    aList = []
    for line in infile:
        line.strip()
        if line[0:4] == "word":
            line = line.replace("word: ","")
            line = line.strip()
            word = line            
        elif line[0:4] == "freq":
            line = line.replace("frequency: ","")
            frequency = int(line)
        elif line[0:4] == "defi":
            index = len(aList)
            line = line.replace("definition: ","")
            definition = line.replace("\n","")
            aList.append([word,definition,frequency])

    return aList

########################################

class Edge:
    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0
    def __str__(self):
        return f"({self.u}, {self.v}, {self.capacity})"
    def __repr__(self):
        return self.__str__()

# finds bottleneck for chosen path
def dfs(u, t, bottleneck):
    if u == t:
        return bottleneck

    visited[u] = True

    # all edges originating from u
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

def allocate(preferences, licences):
    global graph
    # number of people
    ppl_num = len(preferences)

    # find number of locations
    max_loclen = 0
    for preference in preferences:
        for location in preference:
            if location+1>max_loclen:
                max_loclen += 1

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
    edges.append(Edge(sink-1, sink, ppl_num-2*max_loclen))

    for edge in edges:
        reverse_edge = Edge(edge.v, edge.u, 0)
        edge.reverse = reverse_edge
        reverse_edge.reverse = edge
        graph[edge.u].append(edge)
        graph[edge.v].append(reverse_edge)

    max_flow_value = max_flow(graph, source, sink)
    print("Maximum Flow:", max_flow_value)
    if max_flow_value != ppl_num or max_flow_value < 2:
        return None

    # output list
    output = []
    for _ in range(max_loclen):
        output.append([])

    for i in range(1,ppl_num+1):
        for edge in graph[i]:
            if edge.flow == 1:
                output[(edge.v-ppl_num-1)//2].append(edge.u-1)
    return output


class Trie:
    def __init__(self):
        pass



if __name__ == "__main__":
    Dictionary = load_dictionary("Dictionary.txt")
    myTrie = Trie(Dictionary)