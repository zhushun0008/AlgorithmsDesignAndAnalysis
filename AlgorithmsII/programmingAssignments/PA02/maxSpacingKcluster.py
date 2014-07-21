__author__ = 'zhushun0008'

MAX_NUM_VERTICE = 500


def getClusterData(fileName):
    data = open(fileName).readlines()
    edgeInfoList = [tuple(map(int, r.split())) for r in data[1:]]

    return edgeInfoList


def unionFind(clusters, vertex):
    def find(vertex):
        if clusters[vertex] == None:
            return None
        elif None != clusters[vertex] and clusters[vertex] < 0:
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


def maxSpacingCluster(edgeInfoList, kCluster):
    clusters = [None] * (MAX_NUM_VERTICE + 1)
    numEdge = len(edgeInfoList)
    numCluster = 0
    for vertex in edgeInfoList:
        # index in the clusters indicate vertex
        # clusters[3] 3 is the vertex
        # None values represent they are not vertices
        # Negative values indicate roots and number of the negative in the clusters represent number of clusters
        # Positive values indicate parents of this vertices
        # Each vertex is a cluster at the beginning
        clusters[vertex[0]] = -1
        clusters[vertex[1]] = -1

    # get number of vertices
    for cluster in clusters:
        if cluster == -1:
            numCluster += 1

    sortedEdge = sorted(edgeInfoList, key=lambda x: x[2])
    edgeIndex = 0
    while numCluster > kCluster and edgeIndex < numEdge:
        edge = sortedEdge[edgeIndex]
        clusterOne = unionFind(clusters, edge[0])
        clusterTwo = unionFind(clusters, edge[1])
        if clusterOne != clusterTwo:
            clusters = TreeBasedUnion(clusters, clusterOne, clusterTwo)
            numCluster -= 1

        edgeIndex += 1

    return clusters, sortedEdge[edgeIndex:]


def getMaxDistance(clusters, remainEdges):
    leaders = []
    i = 0
    while i < len(clusters):
        if None != clusters[i] and clusters[i] < 0:
            if clusters[i] not in leaders:
                leaders.append(i)
        i += 1

    distanceDict = {}
    print len(leaders)
    for i in range(0, len(leaders) - 1):
        for j in range(i + 1, len(leaders)):
            if leaders[i] < leaders[j]:
                distanceDict[(leaders[i], leaders[j])] = None
            else:
                distanceDict[(leaders[j], leaders[i])] = None

    print distanceDict

    for edge in remainEdges:
        clusterOne = unionFind(clusters, edge[0])
        clusterTwo = unionFind(clusters, edge[1])
        if clusterOne != clusterTwo:
            if clusterOne < clusterTwo:
                if None == distanceDict[(clusterOne, clusterTwo)] or edge[2] < \
                        distanceDict[(clusterOne, clusterTwo)]:
                    distanceDict[(clusterOne, clusterTwo)] = edge[2]
            else:
                if None == distanceDict[(clusterTwo, clusterOne)] or edge[2] < \
                        distanceDict[(clusterTwo, clusterOne)]:
                    distanceDict[(clusterTwo, clusterOne)] = edge[2]

    return distanceDict


# edgeInfoList = getClusterData("clustering1.txt")
edgeInfoList = getClusterData("clustering1.txt")
clusters, remainEdges = maxSpacingCluster(edgeInfoList, 4)

print getMaxDistance(clusters, edgeInfoList)

p