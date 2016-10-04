def longword(inList):
    maxLen = 0
    maxWord = ''
    for iWord in inList:
        if len(iWord)>maxLen:
            maxLen = len(iWord)
            maxWord = iWord
    for i in range(-1,-maxLen-1,-1):
        print(maxWord[i], end='')
    print()
    return maxLen


words = ['zucchini', 'chess', 'pie', 'engine', 'tire']
