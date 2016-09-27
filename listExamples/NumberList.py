def repeatnum(numList):
    newList = []
    for i in range(len(numList)):
        tempList = [numList[i]] * numList[i]
        newList = newList + tempList
    return newList


