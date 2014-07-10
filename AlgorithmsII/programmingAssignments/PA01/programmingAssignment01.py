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
    
    

    
          
jobList = getJobData()   
#scheduledJobList1 = scheduleJobsWithDecreasingDifference(jobList)
#totalcost1 = computeTotalCost(scheduledJobList1)

scheduledJobList2 = scheduleJobsWithDecreaingRatio(jobList)
totalcost2 = computeTotalCost(scheduledJobList2)


