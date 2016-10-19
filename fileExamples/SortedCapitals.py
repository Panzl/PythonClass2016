infile = open('TestData/StateCapitalList.txt','r')
stateData = infile.read()
infile.close()

dataLines = stateData.split('\n')
state = []
capital = []
for line in dataLines:
    if line:
        iState, iCapital = line.split(',')
        state.append(iState)    
        capital.append(iCapital)

outfile = open('TestData/sCapitalList.txt','w')
capital.sort()
for iCap in capital:
    outfile.write(iCap + '\n')

outfile.close()
