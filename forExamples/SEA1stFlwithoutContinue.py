for iFloor in range(1,6):
    for iWing in range(100,401,100):
        if not(iFloor==1 and iWing<300):
            for iRoom in range(26):
                wingRoom = iWing + iRoom
                roomNumber = 'SEA ' + str(iFloor) + '.' + str(wingRoom)
                print(roomNumber)
            
