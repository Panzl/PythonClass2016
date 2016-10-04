def wordlist(inList):
    for iWord in inList:
        if iWord == inList[0]:
            outString = iWord
        elif iWord == inList[-1]:
            outString = outString + ', and ' + iWord
        else:
            outString = outString + ', ' + iWord
    return outString

food = ['apples', 'bananas', 'tofu', 'cheese']
animals = ['cat', 'dog', 'elephant', 'tiger', 'kangaroo']
twolist = ['A', 'B']
