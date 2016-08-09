for iFloor in range(2,6):
    for iWing in range(100,401,100):
        for iRoom in range(26):
            wingRoom = iWing + iRoom
            roomNumber = 'SEA ' + str(iFloor) + '.' + str(wingRoom)
            print(roomNumber)
            
