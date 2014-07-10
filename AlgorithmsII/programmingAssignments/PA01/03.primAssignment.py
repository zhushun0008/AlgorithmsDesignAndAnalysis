# -*- coding: utf-8 -*-
def getEdgeData():
    data =  open("F:\SkyDrive\Studying\coursera\Algorithms_designAndAnalysis\AlgorithmsDesignAndAnalysis\AlgorithmsII\programmingAssignments\PA01\edges.txt").readlines()
    edgeList = [ tuple(map(int, r.split())) for r in data[1:] ]
    return edgeList   
    
 
def getGraphAugmentedAdjList(edgeList) :  
    ## Get all vertices from all edges  
    V1 = []
    V2 = []
    adjacencyList = []
    keyValue = 10000000
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
        
    return Vertices,adjacencyList         
      
        
def primMST(edgeList):
    print "00000"
    V,adjacencyList = getGraphAugmentedAdjList(edgeList)
    
    rootVertex = V[0]
    exploredVertice = [rootVertex]
    print "11111111111111"
    priorityQueue = sorted(adjacencyList[rootVertex-1][1],key=lambda x:x[2])
    adjacencyList[rootVertex-1][0][1] = priorityQueue[0][2]
    unexploredVertice = list(set(V) - set([rootVertex]))
    spanningTreeEdges = []
    #return adjacencyList,priorityQueue
    i = 1
    while len(unexploredVertice) != 0 :
        if priorityQueue : 
            candidateEdge = priorityQueue[0]
            candidateVertex = candidateEdge[1]
    
            priorityQueue.remove(priorityQueue[0])
    
            if candidateVertex in unexploredVertice and adjacencyList[candidateVertex-1][0][1] < candidateEdge[2] :
                exploredVertice = list(set.union(set(exploredVertice),set(candidateVertex)))
                unexploredVertice = list(set(unexploredVertice) - set(candidateVertex))
                spanningTreeEdges.append(candidateEdge)
                
                adjacencyList[candidateVertex-1][0][1] = candidateEdge[2]
                priorityQueue = sorted(priorityQueue + adjacencyList[candidateVertex - 1][1],key = lambda x:x[2])
            
    return spanningTreeEdges       
 

    
edgeList = getEdgeData()
aaa,bbb = primMST(edgeList) 
#V = primMST(edgeList)  