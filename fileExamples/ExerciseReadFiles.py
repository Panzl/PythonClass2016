def readTxt(infile):
    f = open(infile,'r')
    inVar = f.read().strip().split('\n')
    return inVar

def readVar(infile):
    f = open(infile,'r')
    inVar = f.read().strip().split('\n')
    Var = [int(i) for i in inVar]
    return Var

subjID = readTxt('ExerciseDir/subjID.txt')
trialNum = readVar('ExerciseDir/trialNum.txt')
onset = readVar('ExerciseDir/onset.txt')
RT = readVar('ExerciseDir/RT.txt')

# printing out what was read
print('ID\tTrial\tOnset\tRT')
for i in range(len(subjID)):
    print(subjID[i],trialNum[i],onset[i],RT[i],sep='\t')

