def getJobData():
    data = open("F:\SkyDrive\Studying\coursera\Algorithms_designAndAnalysis\AlgorithmsDesignAndAnalysis\AlgorithmsII\programmingAssignments\PA01\jobs.txt").readlines()
    jobList = [ tuple(map(int, r.split())) for r in data[1:] ]
    return jobList 
    
def scheduleJobsWithDecreasingDifference(jobList):
    """
    Input: list of jobs with the tuple of weight and length
    [(4, 38),
    (68, 15)]

    Output:
    """
    scheduledJobList = sorted(jobList,key=lambda x:(x[0]-x[1],x[0]), reverse=True)
    return scheduledJobList

def scheduleJobsWithDecreaingRatio(jobList):
    """
    Input: list of jobs with the tuple of weight and length
    [(4, 38),
    (68, 15)]

    Output:
    """
    scheduledJobList = sorted(jobList,key=lambda x:1.0* x[0] / x[1], \
    reverse=True)
    return scheduledJobList

def computeTotalCost(scheduledJobList):
    """
    Input: list of jobs with the tuple of weight and length
    [(4, 38),
    (68, 15)]

    Output:
    """
    sumCost = 0
    completeTime = 0
    for job in scheduledJobList :
        completeTime += job[1]
        sumCost += job[0] * completeTime
        
    return sumCost    
    
    
def getEdgeData():
    data =  open("F:\SkyDrive\Studying\coursera\Algorithms_designAndAnalysis\AlgorithmsDesignAndAnalysis\AlgorithmsII\programmingAssignments\PA01\edges.txt").readlines()
    edgeList = [ tuple(map(int, r.split())) for r in data[1:] ]
    return edgeList   
    
 
    
def primMST(edgeList):
    V1 = []
    V2 = []
    totalCost = 0
    for edge in edgeList :
        V1.append(edge[0])
        V2.append(edge[1])
    V = set().union(set(V1),set(V2))  
    
    increasedEdgeListByWeights = sorted(edgeList,key=lambda x:[2])
    X = V[0]
    while set(X) != V :
        cheapestEdge = findCheapestEdge(X,V-X,increasedEdgeListByWeights)
        X = set().union(X,cheapestEdge[1])
        totalCost += cheapestEdge[2]
        increasedEdgeListByWeights.remove(cheapestEdge)

    return totalCost       
 
def findCheapestEdge(X,VminusX,edgeList) :
    return edgeList[1]
    
          
jobList = getJobData()   
#scheduledJobList1 = scheduleJobsWithDecreasingDifference(jobList)
#totalcost1 = computeTotalCost(scheduledJobList1)

scheduledJobList2 = scheduleJobsWithDecreaingRatio(jobList)
totalcost2 = computeTotalCost(scheduledJobList2)


edgeList = getEdgeData()
V = primMST(edgeList)