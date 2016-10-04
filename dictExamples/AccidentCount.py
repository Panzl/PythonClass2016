numAccident = {'A':5, 'C':2, 'D':1, 'F':2, 'H':1}
for i in 'ABCDEGFHIJK':
    if i not in numAccident:
        numAccident[i] = 0

for iCar,iCount in numAccident.items():
    print(iCar + ':   ' + str(iCount))
    
