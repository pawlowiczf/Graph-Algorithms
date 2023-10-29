def Push(vertexExcess, vertexHeight, flow, u):
    #
    for v in range( len(flow) ):
        #
        possibleFlow = min( vertexExcess[u], flow[u][v] )
        if v != u and vertexHeight[u] == vertexHeight[v] + 1 and possibleFlow > 0:
            #
            flow[u][v] -= possibleFlow 
            flow[v][u] += possibleFlow

            vertexExcess[u] -= possibleFlow
            vertexExcess[v] += possibleFlow

            return True 
        #end 'if' clause
    #end 'for' loop

    return False 
#end procedure Push()

def Relabel(vertexHeight, flow, u):
    #
    n = len(flow)
    minimumHeight = float('inf')

    for v in range(n):
        #
        if v != u and flow[u][v] > 0:
            minimumHeight = min( minimumHeight, vertexHeight[v] )
        #
    #end 'for loop 

    if minimumHeight >= vertexHeight[u]:
        vertexHeight[u] = 1 + minimumHeight
        return True
    #
    return False
#end procedure Relabel()

def overFlowVertex(vertexExcess, s, t):
    #
    for u in range( len(vertexExcess) ):
        if vertexExcess[u] > 0 and u != s and u != t:
            return u 
    #

    return -1
#end procedure overFlowVertex()

import copy

def PushRelabel(G, s, t):
    #
    n = len(G) 

    vertexExcess = [ 0 for _ in range(n) ]
    vertexHeight = [ 0 for _ in range(n) ]
    flow = copy.deepcopy(G)
    vertexHeight[s] = n - 1

    for u in range(n):
        if G[s][u] > 0 and u != s and u != t:
            flow[s][u] = 0
            flow[u][s] = G[s][u]
            vertexExcess[u] += G[s][u]
            vertexExcess[s] -= G[s][u]
    #end 'for' loop 

    vertex = overFlowVertex(vertexExcess, s, t)
    while vertex != -1:
        #
        if not Push(vertexExcess, vertexHeight, flow, vertex):
            flag = Relabel(vertexHeight, flow, vertex)
        #

        vertex = overFlowVertex(vertexExcess, s, t)
    #end 'while' loop 

    return vertexExcess[t]
#end procedure PushRelabel()

G = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 7, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]
print( PushRelabel(G, 0, 5) ) # 6 


G = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0] ]

print( PushRelabel(G, 0, 5) ) # 23
