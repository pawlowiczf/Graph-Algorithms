#Algorytm Edmondsa-Karpa (szukanie sciezki powieksajacej odbywa sie algorytmem BFS)

from collections import deque 

def BFS(G, source, sink):
    #
    n     = len(G) 

    queue = deque()
    queue.append( source )

    parent  = [ None  for _ in range(n) ]
    visited = [ False for _ in range(n) ]

    while queue:
        #
        vertex = queue.popleft()

        if vertex == sink: return parent 

        for neighbour in range(n):
            if visited[neighbour] == False and G[vertex][neighbour] > 0: 

                parent[neighbour]  = vertex
                visited[neighbour] = True
                queue.appendleft( neighbour ) 

        #end 'for' loop 
    #end 'while' loop 

    return False  
#end procedure BFS()

def augmentPath(G, parent, source, sink):
    #
    bottleNeck  = float('inf')
    pointer     = sink

    while pointer != source:
        bottleNeck = min( bottleNeck, G[ parent[pointer] ][ pointer ] )
        pointer     = parent[ pointer ]
    #end 'while' loop 

    while sink != source:
        #
        G[ parent[sink] ][ sink ] -= bottleNeck
        G[ sink ][ parent[sink] ] += bottleNeck
        sink                       = parent[sink]
    #end 'while' loop 

    return bottleNeck 
#end procedure augmentPath()

def EdmondsKarp(G, source, sink):
    #
    maxFlow = 0
    parent  = BFS(G, source, sink)

    while parent:
        #
        bottleNeck = augmentPath(G, parent, source, sink)
        parent     = BFS(G, source, sink)
        maxFlow   += bottleNeck

    #end 'while' loop
     
    return maxFlow
#end procedure EdmondsKarp()


G = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0] ]

print( EdmondsKarp(G, 0, 5) ) # 23

G = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 7, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]

print( EdmondsKarp(G, 0, 5) ) # 6
