from collections import deque 

class Graph:
    def __init__(self, adjList, n):
        self.n       = n
        self.pairU   = [ n for _ in range(n) ]
        self.pairV   = [ n for _ in range(n) ]
        self.adjList = adjList 
#end class Graph

def BFS(G, distance):
    #
    queue = deque()

    for vertex in range( G.n ):

        if G.pairU[ vertex ] == G.n:

            queue.append( vertex )
            distance[vertex] = 0

        #end 'if' clause 
    #end 'for' loop 

    while queue:
        #
        vertex = queue.popleft()

        if vertex != G.n:
            for neighbour in G.adjList[ vertex ]:

                if distance[ G.pairV[neighbour] ] == float('inf'):

                    queue.append( G.pairV[ neighbour ] )
                    distance[ G.pairV[neighbour] ] = distance[ vertex ] + 1 
                
                #end 'if' clause 
            #end 'for' loop 
    #end 'while' loop 

    return distance[ G.n ] != float('inf')
#end procedure BFS()

def DFS(G, distance, vertex):
    #
    if vertex != G.n:
        #
        for neighbour in G.adjList[vertex]:
            if distance[ G.pairV[neighbour] ] == distance[ vertex ] + 1:

                if DFS(G, distance, G.pairV[neighbour] ):
                    G.pairU[vertex]    = neighbour
                    G.pairV[neighbour] = vertex
                    return True 
                #end 'if' clause 
            #end 'if' clause 
        #end 'for' loop 

        distance[vertex] = float('inf')
        return False 
    #end 'if' clause 

    return True 
#end procedure DFS()

def HopcroftKarp( adjList ):
    #
    G = Graph( adjList, len(adjList) )
    matching = 0 

    distance = [ float('inf') for _ in range(G.n + 1) ]

    while BFS(G, distance):
        #
        for vertex in range(G.n):
            if G.pairU[ vertex ] == G.n and DFS(G, distance, vertex):
                matching += 1 
        #end 'for' loop

        distance = [ float('inf') for _ in range( G.n + 1 ) ] 
    #end 'while' loop 

    return matching
#end procedure HopcroftKarp()


adjList = [ [ 0, 1, 3], [ 2, 4],[ 0, 2],[ 3 ], [ 3, 2] ]
print( HopcroftKarp( adjList ) )


