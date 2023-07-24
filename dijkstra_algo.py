def lowest_node(costs):
    lowest = infinity
    lowest_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest and node not in processed:
            lowest = cost
            lowest_node = node
    
    return lowest_node

def findWay(final):
    path = [final]
    CHANGE = True

    while CHANGE:
        CHANGE = False
        for x in parents:
            if x == path[-1]:
                path.append(parents[x])
                CHANGE = True
        
    return path[::-1]

def dijkstra(final):
    node = lowest_node(costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for neighbor in neighbors:

            new_cost = cost + neighbors[neighbor]

            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        
        processed.append(node)
        node = lowest_node(costs)
    
    way = findWay(final)

    try:
        if costs[final] == 0:
            return 0, None
        return costs[final], way
    except KeyError:
        return None, None



processed = []

graph = {}

graph["start"] = {}
graph["start"]["A"] = 5
graph["start"]["E"] = 1

graph["A"] = {}
graph["A"]["B"] = 10
graph["A"]["C"] = 7

graph["B"] = {}
graph["B"]["D"] = 2

graph["C"] = {}
graph["C"]["B"] = 3
graph["C"]["finish"] = 1

graph["D"] = {}
graph["D"]["B"] = 2
graph["D"]["finish"] = 5

graph["E"] = {}
graph["E"]["C"] = 3
graph["E"]["D"] = 6

graph["finish"] = {}


infinity = float("inf")

costs = {}
costs["A"] = 5
costs["B"] = infinity
costs["C"] = infinity
costs["D"] = infinity
costs["E"] = 1
costs["finish"] = infinity

parents = {}
parents["A"] = "start"
parents["E"] = "start"
parents["B"] = None
parents["C"] = None
parents["D"] = None
parents["finish"] = None

arg = input(str("To which node you want to find the way and cost? "))

if dijkstra(arg)[0] == None and dijkstra(arg)[1] == None:
    print("Wrong node")
elif dijkstra(arg)[0] == 0 and dijkstra(arg)[1] == None:
    print("There is no path to this node")
else:
    print("The fastest way from start to finish is: ", dijkstra(arg)[0], "\nPath is: ", dijkstra(arg)[1], "\nEdges:", len(dijkstra(arg)[1])-1)

