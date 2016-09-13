startTime = 0
endTime = 121
stepTime = 10
charge = 16
for iTime in range(startTime, endTime, stepTime):
    print('The phone is ' + str(charge) + '% charged at ' + str(iTime) + ' min')
    charge += 3
