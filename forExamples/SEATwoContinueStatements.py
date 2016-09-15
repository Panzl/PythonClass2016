for iFloor in range(1,7):
    for iWing in range(100,401,100):
        if iFloor==1 and iWing<300:
            continue
        if iFloor==6 and iWing>100:
            continue
        for iRoom in range(26):
            wingRoom = iWing + iRoom
            roomNumber = 'SEA ' + str(iFloor) + '.' + str(wingRoom)
            print(roomNumber)
            
