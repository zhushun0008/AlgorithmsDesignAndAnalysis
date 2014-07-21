__author__ = 'zhushun0008'
import sys
sys.setrecursionlimit(10000)


def unionFind(clusters, vertex):
    def find(vertex):
        if clusters[vertex] < 0:
            return vertex
        else:
            clusters[vertex] = find(clusters[vertex])
            return clusters[vertex]

    return find(vertex)


def TreeBasedUnion(clusters, clusterOne, clusterTwo):
    if clusters[clusterOne] < clusters[clusterTwo]:
        clusters[clusterTwo] += clusters[clusterOne]
        clusters[clusterOne] = clusterTwo
    else:
        clusters[clusterOne] += clusters[clusterTwo]
        clusters[clusterTwo] = clusterOne

    return clusters


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
        for j in range(i):
            if oneBitFlip & (1 << j):
                twoBitFlip = oneBitFlip - (1 << j)
            else:
                twoBitFlip = oneBitFlip + (1 << j)
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
    def DFS_Visit(vertex, adjDict, visitedMark, clusters, numCluster):
        visitedMark[vertex] = True
        for adjVertex in adjDict[vertex]:
            if clusters.has_key(adjVertex):
               # print adjVertex
                #print clusters.has_key(adjVertex)
                if visitedMark[adjVertex] == False:
                    clusterOne = unionFind(clusters, vertex)
                    clusterTwo = unionFind(clusters, adjVertex)
                    if clusterOne != clusterTwo:
                        clusters = TreeBasedUnion(clusters, clusterOne, clusterTwo)
                        numCluster -= 1
                        DFS_Visit(adjVertex, adjDict, visitedMark, clusters, numCluster)
        return visitedMark, clusters, numCluster

    clusters = {}
    visitedMark = {}
    for vertex in vertexList:
        clusters[vertex] = -1
        visitedMark[vertex] = False

    numCluster = len(clusters)
    for vertex in vertexList:
        if visitedMark[vertex] == False:
           visitedMark, clusters, numCluster = DFS_Visit(vertex, adjDict, visitedMark, clusters, numCluster)
    numCluster = 0
    for e in clusters:
        if clusters[e] < 0:
            numCluster += 1
    return numCluster


vertexList = getClusterData("clustering_big.txt")
adjDict = makeAdjList(vertexList)
print getLeastNumClusters(vertexList, adjDict)


