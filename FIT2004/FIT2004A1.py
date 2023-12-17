# Author = Brian Wu
# Student ID = 33116075
# Last edited = 14/09/23

import heapq as heap

def restaurantFinder(d: int, site_list: list) -> tuple:
    """
    Function description: function in order to find the largest possible revenue from restaurants that have an
    annual revenue specified in site_list where chosen restaurants need to be a certain distance apart from 
    each other specified by the distance parameter (d)

    Approach description:
    First start with the max profits for the first d restaurants which are just the maximum profit of the first d
    Then check potential new max profit by adding the max profit of last chosen site and new site
    If new potential max profit is larger than previous max profit, then make it the new max profit
    Then last max profit is the largest possible revenue and chosen sites is found based off max_profit list


    :Input: 
        d (int): the minimum distance parameter specified between the chosen restaurants
        site_list (list): the list of the annual revenue for each restaurant site

    :Output:
        (overall_max_profit, chosen_restaurants) (tuple (int, list)): 
            tuple containing the max profit possible and restaurants chosen to get that max profit


    :Time complexity: O(N + N + N-d-1 + N) = O(4N-d-1) =  O(N)

    :Aux space complexity: O(N + N) = O(N)
    """

    # Initialise a list which will contain the max profit for up to each restaurant
    # This is basically the max profit that can be made for the restaurants prior to and including current restaurant 
    # given gap restrictions (d)
    # TIme complexity: O(N), where N is number of sites
    # Aux space complexity: O(N), where N is number of sites
    max_profits = [0] * len(site_list)
    
    # For first d restaurants, max profits will just be the restaurant with largest revenue for each restaurant
    # Min of d+1 and len(site_list) is just in case d is larger than the number of sites
    # Time complexity: O(N), where N is number of sites
        # loops d + 1 times or N times
    for i in range(min(d + 1, len(site_list))):
        if site_list[i] > max_profits[i-1]:
            max_profits[i] = site_list[i]
        else:
            max_profits[i] = max_profits[i-1]

    # After we have the first d max profits, 
    # the previous max_profit and the previous selected restaurant's (j-d-1 is previous selected restaurant) max profit
    # plus the new potential restaurant's revenue is compared, this is the potential new max profit
    # Time complexity: O(N - d - 1), where N is length of input list and d is distance specified
        # loops N - d - 1 times, does not run if d is larger than site list
    for j in range(d + 1, len(site_list)):
        # If previous max profit is larger than the potential new max profit, make current max profit = previous max profit
        if max_profits[j-1] > max_profits[j-d-1] + site_list[j]:
            max_profits[j] = max_profits[j-1]
        # If it is less, then this means new restaurant is chosen hence make current max profit = potential new max profit
        else:
            max_profits[j] = max_profits[j-d-1] + site_list[j]
    
    # Getting site lists from max_profits list
    # Time complexity: O(N) worst case where N is number of sites
    # Aux space complexity: O(N) where N is number of sites
    restaurants = []  
    k = len(site_list)-1
    while k>=0:
        # Case of first site being chosen
        if k == 0 and max_profits[0]>0:
            restaurants.append(1)
        # Starting from end of max profits list, if current (k) max profit larger than previous (k-1),
        # this means current restaurant was chosen (k+1 is restaurant number), then check last chosen site (k-d-1)
        if max_profits[k]> max_profits[k-1]:
            restaurants.append(k+1)
            k = k-d-1
        # If current not larger than previous, then current was not chosen so check next potentially chosen site (k-1)
        else:
            k = k-1

    # List reversal O(N) time complexity, where N is number of sites
    overall_max_profit = max_profits[-1]
    chosen_restaurants = restaurants[::-1]
    return (overall_max_profit, chosen_restaurants)

class FloorGraph:
    """
    Graph class representing the paths, nodes and keys in the graph specified upon initialisation
    Functions: 
        __init__: function called upon intialisation
        climb: function for finding the fastest path from start to exit and getting key
    """
    def __init__(self, paths: list, keys: list) -> None:
        """
        Function description: Initialisation function of the FloorGraph class, initialises the structure of the graph

        Approach description: The approach takes the graph structure and layers a copy of the graph on top, the two
        laters are connected by paths which connect the key nodes to their copy via a path with length of the time
        it takes to get the key by defeating the monster

        :Input:
            paths (list): the paths specified in the graph, has form (u,v,x) where u is starting node ID, v is ending node ID
            and x is the time it takes to traverse u to v
            keys (list): the list of keys and the time it takes to get each key

        :Output:
            None

        :Time complexity: O(E + V + E + V) = O(2E + 2V) = O(E + V)
            where E is the set of paths and V is the number of unique locations

        :Aux space complexity: O(V + E)
            where E is the set of paths and V is the number of unique locations
            It is V + E as the adjacency list has V elements of pointers to E amount of lists which all have constant size in memory
        """

        # Get the total number of nodes by finding the max node
        # Time complexity: O(E), where E is the set of paths
        current_max_node = 0
        for path in paths:
            current_max_node = max(path[0], path[1], current_max_node)
        self.num_nodes = current_max_node + 1 # total number of nodes

        # Initialise adjacency list
        # Require double the size of number of nodes for the two layers of graph
        # Time complexity: O(2V) = O(V), where V is the number of unique locations
        # Aux space complexity: O(2V) = O(V), where V is the number of nunique locations
        self.adjacencyList = []
        for _ in range(2*self.num_nodes):
            self.adjacencyList.append([])

        # Adds paths to adjacency list in form [v, x], where v is the destination node ID and x is the time taken to reach it
        # Each index refers to the node number, ie index 1 refers to node ID 1 and contains the paths leacing node ID 1
        # The first half contains the original graph, the second half contains the nodes of the copy of the graph
        # Time complexity: O(E), where E is the set of paths
        # Aux space complexity: O(2E) = O(E), where E is the set of paths
        for path in paths:
            self.adjacencyList[path[0]].append([path[1], path[2]])
            self.adjacencyList[path[0]+self.num_nodes].append([path[1]+self.num_nodes, path[2]])
        
        # Adds the paths from the graph to the second layer with keys, where the length is time taken to get key
        # Time complexity: O(V), where V is the number of unique locations
        for key in keys:
            self.adjacencyList[key[0]].append([key[0]+self.num_nodes, key[1]])

    def climb(self, start: int, exits: list) -> tuple:
        """
        Function description: Function to find the shortest path from the start to an exit given that a key is gotten

        Approach description: Apply Dijikstra's algorithm on the two layer graph and find the minimum path of the exits
        Search through the second half of the Dijikstra's output since the elements there represent the nodes given a key is gotten

        :Input:
            start (int): the starting node ID
            exits (list): a list of all possible exit node IDs

        :Output:
            (fastestTime, path_taken) (tuple(int, list)): tuple with the fastest time to get from start to an exit and the path that it takes

        :Time complexity: O(V + Elog(V) + V + E + E) = worst case O(Elog(V)) where E is the set of paths and V is the number of unique locations 

        :Aux space complexity: O(V + V + E + E + E) = O(V + E) where E is the set of paths and V is the number of unique locations

        """
        # Initialise the times_taken list, which shows the min time it takes to go from the start node to each node
        # Initialise the predecessor list, which shows the previous node for each node
        # Time complexity: O(2V) = O(V), where V is the number of unique locations
        # Aux space complexity: O(2V) = O(V), where V is the number of unique locations 
        times_taken = []
        predecessor = []
        for _ in range(2*self.num_nodes):
            times_taken.append(float('inf'))
            predecessor.append(None)
            
        # Initialise the starting time (it takes 0 minutes to go from start to start)
        times_taken[start] = 0

        # Initialise priority queue for Dijikstra's algorithm which will have the next nodes to search for min distance vertex
        queue = [[start,0]]

        # If the queue is not empty, there are still nodes to be searched
        # Start of Dijikstra's algorithm
            # Time complexity: O(Elog(V)), where E is the set of paths and V is the number of unique locations
            # Aux space complexity: O(V + E), where E is the set of paths and V is the number of unique locations
        while len(queue) != 0:
            # First node in queue is the next one to be searched
            current_node, node_time = heap.heappop(queue)

            # If this node has been searched, skip it
            if node_time > times_taken[current_node]:
                continue
            
            # Update the times of the adjacent nodes
            for adjacent_node, weight in self.adjacencyList[current_node]:
                # If it is faster to take adjacent node to reach current node, update the time taken
                if times_taken[current_node] + weight < times_taken[adjacent_node]:
                    times_taken[adjacent_node] = times_taken[current_node] + weight
                    # Push next node to be searched
                    heap.heappush(queue, [adjacent_node, times_taken[adjacent_node]])
                    # Update the predecessor of the adjacent node to current node if it is faster
                    predecessor[adjacent_node] = current_node
                # else: do not update time taken

        # Find the fastest time and the exit associated with it
        # Time complexity: O(V) worst case, where V is the number of unique locations
        fastestTime = float('inf')
        fastestExit = None
        for exit in exits:
            # Of the specified exits, exit+self.num_nodes gets the exits in the copy of the graph, which is the second half of the list
            if times_taken[exit+self.num_nodes] < fastestTime:
                fastestTime = times_taken[exit+self.num_nodes]
                fastestExit = exit

        # In case there is no possible path
        if fastestExit == None:
            return None

        # Finds the path taken
        # Time complexity: O(E) worst case, where E is the set of paths
        # Aux space complexity: O(E) worst case, where E is the set of paths
        path = []
        current = fastestExit+self.num_nodes
        # Stop when start node reached
        while current != None:
            # If in second half, append appropriate node ID
            if current >= self.num_nodes:
                path.append(current-self.num_nodes)
            # If this node didn't come from a key or if it is the first element
            elif path == [] or current != path[-1]:
                path.append(current)
            # Search next node
            current = predecessor[current]

        # Time complexity: O(E) worst case, where E is the set of paths
        path_taken = path[::-1]
        return (fastestTime, path_taken)