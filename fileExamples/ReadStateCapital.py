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

