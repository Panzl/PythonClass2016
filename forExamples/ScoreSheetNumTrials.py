for iCond in range(1,5):
    print('Condition: ' + str(iCond))
    if iCond==1 or iCond==4:
        numTrial = 20
    else:
        numTrial = 10
    for iTrial in range(1,numTrial+1):
        print('     Trial: ' + str(iTrial) + '  ' + '_'*15)

        
