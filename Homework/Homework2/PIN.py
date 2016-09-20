PIN = 2227
numEntry = 0
while True:
    print('Please enter the PIN')
    userPIN = int(input())
    numEntry += 1
    if userPIN == PIN:  # if correct PIN entered, print message and break
        print('Access granted!')
        break
    elif numEntry<5:  # if before 5th try, go back to the beginning
        continue
    else:  # if the 5th try, then print message and break
        print('Too many attempts, account frozen!')
        break

