import copy

def DeCat(origList):
    newList = copy.copy(origList)
    while 'cat' in newList:
        newList.remove('cat')
    return newList

mammal = ['cat', 'dog', 'cat', 'cat', 'tiger']
mammalNoCat = DeCat(mammal)
