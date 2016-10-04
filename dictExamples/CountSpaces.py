message = 'the quick brown fox jumps over the lazy dog'
count = {}   # initializing the counter
for iLetter in message:
    count.setdefault(iLetter,0)
    count[iLetter] += 1

countSpace = 0
countLetter = 0
for iLetter, iCount in count.items():
    if iLetter == ' ':
        countSpace += iCount
    else:
        countLetter += iCount

print('Number of letters: ' + str(countLetter))
print('Number of spaces: ' + str(countSpace))

