bodyTemp = 96
for iTime in range(0,241,30):
    print(str(iTime) + ' min post-mortem, body temperature:' + str(bodyTemp))
    bodyTemp -=8
