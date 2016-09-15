for i in range(1,10):
    for j in range(1,i+1):
        if j == 1 or j == i:
            print(str(i) * i)
        else:
            print(str(i) + ' '*(i-2) + str(i))
    print()
