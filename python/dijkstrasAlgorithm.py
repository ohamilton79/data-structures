#ohamilton79
#Dijkstra's algorithm
#20/01/2021

import time
#Uses functionality defined in 'minPriorityQueue.py' file
from minPriorityQueue import MinPriorityQueue

#Perform Dijkstra's algorithm
def dijkstra(graph, startNode, endNode):
    #Create a dictionary containing previously vistited vertices, in order to construct the final path
    predecessor = {}
    #Create a dictionary containing the costs for each vertex (distance from start)
    costs = {}

    #Create a priority queue of unvisited vertices
    vertexQueue = MinPriorityQueue([], len(graph))

    #Initialise the starting cost of each node as infinity, and add it to the priority queue
    for vertex in graph:
        if vertex != startNode:
            vertexQueue.insertItem(float("inf"), vertex)
            costs[vertex] = float("inf")
            
        #...except the start node, which has a cost of 0
        else:
            vertexQueue.insertItem(0, vertex)
            costs[vertex] = 0

    #While there are still vertices in the priority queue
    while not vertexQueue.isEmpty():
        #Get the next vertex to visit
        currentVertex = vertexQueue.extractMinPriority()
        
        #Iterate over adjacent vertices
        for adjacentVertex in graph[currentVertex[1]]:
            #If the node isn't visited
            if vertexQueue.contains(adjacentVertex):
                #Get the new cost of going through the current node to get to the adjacent vertex
                newCost = currentVertex[0] + graph[currentVertex[1]][adjacentVertex]
                
                #If this new cost is less than the currently stored cost for this adjacent node, update it
                if newCost < vertexQueue.getPriority(adjacentVertex):
                    #Decrease this node's key to the new cost
                    vertexQueue.decreaseKey(adjacentVertex, newCost)

                    #Update cost in dictionary
                    costs[adjacentVertex] = newCost

                    #Save the predecessor vertex
                    predecessor[adjacentVertex] = currentVertex[1]

    #Construct the shortest path using the generated predecessor vertices
    currentNode = endNode
    shortestPath = ""

    while currentNode != startNode:
        #Prepend node to shortest path string
        shortestPath = "-" + currentNode  + shortestPath
        #Get next node
        currentNode = predecessor[currentNode]

    #Complete the path string
    shortestPath = currentNode + shortestPath

    #Return the shortest path and its distancde
    return (shortestPath, costs[endNode])

begin = time.time()

#Set up a sample (undirected) weighted graph as a 2D dictionary
graph = {}
graph["a"] = {}
graph["b"] = {}
graph["c"] = {}
graph["d"] = {}
graph["e"] = {}

#Add weights
graph["a"]["b"] = 5
graph["a"]["c"] = 4
graph["a"]["d"] = 2
graph["b"]["a"] = 5
graph["b"]["c"] = 3
graph["c"]["b"] = 3
graph["c"]["a"] = 4
graph["c"]["d"] = 3
graph["d"]["a"] = 2
graph["d"]["c"] = 3
graph["c"]["e"] = 4
graph["e"]["c"] = 4

#Test data
print(dijkstra(graph, "a", "e"))

end = time.time()
print("Time taken: {}".format(end - begin))

