# -*- coding: utf-8 -*-
def getEdgeData():
    data =  open("F:\SkyDrive\Studying\coursera\Algorithms_designAndAnalysis\AlgorithmsDesignAndAnalysis\AlgorithmsII\programmingAssignments\PA01\edges.txt").readlines()
    edgeList = [ tuple(map(int, r.split())) for r in data[1:] ]
    return edgeList   
    
 
def getGraphAugmentedAdjList(edgeList) :
    """
    
    
    outputs:
        1. Vertices - all vertices in the graph
        2. adjacencyList - [[vertex1 key keyToEdgeIndex],[(edge1Info),(adge2Info)...,(adgenInfo)],
                            [vertex2 key keyToEdgeIndex],[(edge1Info),(adge2Info)...,[adgenInfo],
                                    ......
                                    
                            ]
          
    
    """
    ## Get all vertices from all edges  
    V1 = []
    V2 = []
    adjacencyList = []
    keyValue = 10000000000
    keyToEdgeIndex = None
    for edge in edgeList :
        V1.append(edge[0])
        V2.append(edge[1])
        Vertices = list(set().union(set(V1),set(V2))) 
    for vertex in Vertices :
        temp = [[vertex,keyValue,keyToEdgeIndex],[]]
        adjacencyList.append(temp)
        #print vertex
    for edge in edgeList :
        adjacencyList[edge[0]-1][1].append(edge)
        switchedEdge = (edge[1],edge[0],edge[2])
        adjacencyList[edge[1]-1][1].append(switchedEdge)

    return Vertices,adjacencyList         
      
        
def primMST(edgeList):
    print "00000"
    V,adjacencyList = getGraphAugmentedAdjList(edgeList)
    
    rootVertex = V[20]
    exploredVertice = [rootVertex]
    print "11111111111111"
    priorityQueue = sorted(adjacencyList[rootVertex-1][1],key=lambda x:x[2])
    #print priorityQueue
    adjacencyList[rootVertex-1][0][1] = priorityQueue[0][2]
    unexploredVertice = list(set(V) - set([rootVertex]))
    spanningTreeEdges = []
    #return adjacencyList,priorityQueue
    while len(unexploredVertice) and len(priorityQueue):
        candidateEdge = priorityQueue[0]
        candidateVertex = candidateEdge[1]

        priorityQueue.remove(priorityQueue[0])

        if candidateVertex in unexploredVertice and adjacencyList[candidateVertex-1][0][1] > candidateEdge[2] :
            exploredVertice = list(set.union(set(exploredVertice),set([candidateVertex])))
            unexploredVertice = list(set(unexploredVertice) - set([candidateVertex]))
            spanningTreeEdges.append(candidateEdge)

            adjacencyList[candidateVertex-1][0][1] = candidateEdge[2]
            priorityQueue = priorityQueue+adjacencyList[candidateVertex - 1][1]
            #print(priorityQueue)
            priorityQueue = sorted(priorityQueue,key = lambda x:x[2])
            #print(priorityQueue)
            
    return spanningTreeEdges       
 

    
edgeList = getEdgeData()
spanningTreeEdges = primMST(edgeList)
result = 0
for edge in spanningTreeEdges :
    result += edge[2]

#result = sum([SpanningEdge[2] for SpanningEdge in spanningTreeEdges])

print result
#V = primMST(edgeList)  