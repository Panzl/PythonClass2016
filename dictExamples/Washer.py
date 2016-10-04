washer = {'soak':10, 'wash':20, 'rinse':12, 'spin':6}

print('Washer cycles:')
for i in washer.keys():
    print(i)

sumTime = 0
for i in washer.values():
    sumTime += i
print('Total required time: ' + str(sumTime) +' min')

print('Time required for each cycle:')
for iKey, iValue in washer.items():
    print(iKey + ':   ' + str(iValue) + ' min')

