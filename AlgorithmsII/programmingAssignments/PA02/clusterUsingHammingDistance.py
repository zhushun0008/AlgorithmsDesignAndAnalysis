__author__ = 'zhushun0008'


def getClusterData(fileName):
    data = open(fileName).readlines()
    vertexRawInfoList = [tuple(map(int, r.split())) for r in data[1:]]
    vertexList = []
    for vertex in vertexRawInfoList:
        temp = 0
        for num in vertex:
            temp <<= 1
            temp += num
        vertexList.append(temp)

    return vertexList


def getVertexListWithHS(vertex, lenCoding):
    adjList = []
    for i in range(lenCoding):
        if vertex & (1 << i):
            oneBitFlip = vertex - (1 << i)
        else:
            oneBitFlip = vertex + (1 << i)

        adjList.append(oneBitFlip)
        for j in range(1, 1 << i):
            if oneBitFlip & (1 << j):
                twoBitFlip = oneBitFlip - (1 << j)
            else:
                twoBitFlip = oneBitFlip - (1 << j)
            adjList.append(twoBitFlip)

    return adjList

def makeAdjList(vertexList):
    adjDict = {}

    for vertex in vertexList:
        adjDict[vertex] = getVertexListWithHS(vertex, 24)
    return adjDict

# def get_bit_one(num):
#     result = 0
#     while num != 0:
#         num = num & (num - 1)
#         result += 1
#     return result

# print get_bit_one(15)


def getLeastNumClusters(vertexList, adjDict):
    visitedMark = {}
    for vertex in vertexList:
        visitedMark[vertex] = 0

    def DFS_Visit(vertex, adjDict):
        for adjVex in adjDict[vertex]:
            if visitedMark[adjVex] == 0:
                visitedMark[adjVex] = 1
                DFS_Visit(adjVex, adjDict)

    numCluster = 0
    for vertex in visitedMark.keys():
        if visitedMark[vertex] == 0:
            numCluster += 1
            DFS_Visit(vertex, adjDict)

    return numCluster


vertexList = getClusterData("clustering_big.txt")
adjDict = makeAdjList(vertexList)
print getLeastNumClusters(vertexList, adjDict)


