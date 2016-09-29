import copy

def SortList(origList):
    newList = copy.copy(origList)
    newList.sort()
    return newList

mammal = ['dog', 'cat', 'panda', 'lion', 'horse']
mammalSorted = SortList(mammal)
