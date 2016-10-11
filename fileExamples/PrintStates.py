
f = open('TestData/StateList.txt', 'r')
line = f.readline()
f.close()

States = line.split(',')
for iState in States:
    print(iState)

