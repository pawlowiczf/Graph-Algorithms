from queue import PriorityQueue
# from CheckTests import kod 

# O( VE + V^2logV )

class Node:
    def __init__(self):
        self.isDeactivated = 0
        self.mergedInto    = set()
        self.edges = {}
    #
        
    def addEdge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight 
    #
        
    def delEdge(self, to):
        del self.edges[to]
    #
# end class()
        
def createGraph(V, L):
    #
    G = [ Node() for _ in range(V) ]

    for (vertex, neighbour, weight) in L:
        G[vertex - 1].addEdge(neighbour - 1, weight) 
        G[neighbour - 1].addEdge(vertex - 1, weight)
    #
    
    return G 
# end procedure createGraph()

def fillPriorityQueue(G, weights, queue):
    #
    vertex = 0
    for neighbour in G[vertex].edges: 
        queue.put( ( -G[vertex].edges.get(neighbour), neighbour ) )
        weights[neighbour] += G[vertex].edges.get(neighbour)
    #

    return queue 
# end procedure fillPriorityQueue()

def mergeVertices(G, x, y):
    #
    G[y].isDeactivated = 1
    G[x].mergedInto.add(y)

    if G[x].edges.get(y,-1) != -1:
        G[x].delEdge(y)
        G[y].delEdge(x)
    #

    toRemove = []

    for neighbour in G[y].edges:
        G[x].addEdge( neighbour, G[y].edges[neighbour] )
        G[neighbour].addEdge( x, G[y].edges[neighbour] )
        toRemove.append(neighbour)

    for neighbour in toRemove:
        G[y].delEdge( neighbour )
        G[neighbour].delEdge(y)
 
# end procedure mergeVertices()
    
def minimumCutPhase(G, numberVertices):
    #
    weights    = [ 0 for _ in range( len(G) ) ]

    queue = PriorityQueue()
    queue = fillPriorityQueue(G, weights, queue)

    lastTwoAdded = [ None for _ in range(2) ]
    lastTwoAdded[1] = 0

    currentSet = set() 
    currentSet.add(0) 

    while len( currentSet ) < numberVertices: 
        #
        value, vertex = queue.get(block = False) 
        if vertex in currentSet: continue 

        currentSet.add(vertex)
        
        for neighbour in G[vertex].edges: 
            if neighbour not in currentSet:
                weights[neighbour] += G[vertex].edges.get(neighbour)
                queue.put( ( -weights[neighbour], neighbour ) )
        
        # end 'for' loop 

        lastTwoAdded[0] = lastTwoAdded[1] 
        lastTwoAdded[1] = vertex 
    # end 'while' loop 

    mergeVertices( G, lastTwoAdded[0], lastTwoAdded[1] )
    return weights[ lastTwoAdded[1] ]
# end procedure minimumCutPhase()

def findingMinCut(V, L):
    #
    G = createGraph(V, L)

    numberVertices = len(G) 
    minCutValue = float('inf')

    while numberVertices > 1: 
        #
        value = minimumCutPhase(G, numberVertices)
        minCutValue = min( minCutValue, value )

        numberVertices -=1 
    # end 'while' loop  
    
    return minCutValue
# end procedure findingMinCut() 

# kod( findingMinCut )       
    