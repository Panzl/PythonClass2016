numAccident = {'A':5, 'C':2, 'D':1, 'F':2, 'H':1}
newAccidents = ['A', 'H', 'H', 'D', 'K', 'J']
for i in newAccidents:
    numAccident.setdefault(i,0)
    numAccident[i] +=1

for iCar,iCount in numAccident.items():
    print(iCar + ':   ' + str(iCount))

