import csv

f = open('TestData/StateCapitalList.csv','r')
reader = csv.DictReader(f)
state = []
capital = []
for row in reader:
    state.append(row['State'])
    capital.append(row['Capital'])

f.close()


for i,istate in enumerate(state):
    print('State: ' + '%-15s' % istate + '\tCapital: ' +capital[i])
    
