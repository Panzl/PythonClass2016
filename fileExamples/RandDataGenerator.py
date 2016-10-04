import random

subjID = ['001', '003', '005', '007', '009', '011']
trialNum = list(range(1,6))
stimTime = list(range(35,76,10))

for iSubj in subjID:
    outFile = 'TestDir/sub' + iSubj + '.txt'
    f = open(outFile, 'w')
    for j,jTime in enumerate(stimTime):
        line = '  ' + str(trialNum[j]) + '  ' + str(jTime)
        line += '  ' + str(random.randint(85,110)) + '  \n'
        f.write(line)
    f.close()

