__author__ = 'zhushun0008'

def getData(fileName):
    data = open(fileName).readlines()
    formatedData = [tuple(map(int, r.split())) for r in data]
    KNAPSACK_SIZE = formatedData[0][0]
    ITEM_NUM = formatedData[0][1]
    snapValueWeightData = formatedData[1:]

    return snapValueWeightData, KNAPSACK_SIZE, ITEM_NUM


def knapsack(snapValueWeightData, KNAPSACK_SIZE, ITEM_NUM):
    solutionArray = [[0 for row in range(ITEM_NUM + 1)] for col in range(KNAPSACK_SIZE + 1)]


    for item in range(1, ITEM_NUM + 1):
        for x in range(KNAPSACK_SIZE + 1):
            weight = snapValueWeightData[item - 1][1]
            value = snapValueWeightData[item - 1][0]
            if x - weight < 0 or solutionArray[x][item - 1] > (solutionArray[x-weight][item - 1] + value):
                solutionArray[x][item] = solutionArray[x][item - 1]
            else:
                solutionArray[x][item] = solutionArray[x-weight][item - 1] + value

    return solutionArray


def knapsackForBigData(snapValueWeightData, KNAPSACK_SIZE, ITEM_NUM):
    capcityArray = [0 for col in range(KNAPSACK_SIZE + 1)]
    solutionArray = [0 for col in range(KNAPSACK_SIZE + 1)]


    for item in range(1, ITEM_NUM + 1):
        for x in range(KNAPSACK_SIZE + 1):
            weight = snapValueWeightData[item - 1][1]
            value = snapValueWeightData[item - 1][0]
            if x - weight < 0 or capcityArray[x] > (capcityArray[x-weight] + value):
                solutionArray[x] = capcityArray[x]
            else:
                solutionArray[x] = capcityArray[x-weight] + value
        capcityArray = solutionArray[:]
    return solutionArray
# snapValueWeightData, KNAPSACK_SIZE, ITEM_NUM = getData("knapsack1.txt")
# solutionArray = knapsack(snapValueWeightData, KNAPSACK_SIZE, ITEM_NUM)
# print solutionArray[KNAPSACK_SIZE][ITEM_NUM]

snapValueWeightData, KNAPSACK_SIZE, ITEM_NUM = getData("knapsack_big.txt")
solutionArray = knapsackForBigData(snapValueWeightData, KNAPSACK_SIZE, ITEM_NUM)
print solutionArray[KNAPSACK_SIZE]