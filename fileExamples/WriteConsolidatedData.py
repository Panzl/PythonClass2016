import os

def readfile(fName):
    # open file
    infile = open(fName,'r')
    # initialize variables
    trial = []
    onsetTime = []
    respTime = []
    # read the first line
    line = infile.readline()
    # keep reading files until the last line
    while line:
        inString = line.strip().split()
        inNumber = [int(i) for i in inString]
        trial.append(inNumber[0])
        onsetTime.append(inNumber[1])
        respTime.append(inNumber[2])
        # read the next line
        line = infile.readline()
    return trial, onsetTime, respTime


# changing the working directory to the appropriate directory
WorkDir = 'TestDir'  #this needs to be customized
os.chdir(WorkDir)

# checking the content of the directory
listFiles = os.listdir()
for iFile in listFiles:
    if not (iFile[:3] == 'sub' and iFile[3:6].isdecimal()):
        listFiles.remove(iFile)


# initializing the variables
subjID = []
trialNum = []
onset = []
RT = []

# for loop to read files and store data
for iFile in listFiles:
    iTrial, iOnset, iRT = readfile(iFile)
    iSubj = [iFile.replace('sub','').replace('.txt','')] * len(iTrial)
    subjID += iSubj
    trialNum+= iTrial
    onset += iOnset
    RT += iRT


outfile = open('sub_all.txt','w')
for i in range(len(subjID)):
    outString = subjID[i] + '\t'
    outString += (str(trialNum[i]) + '\t')
    outString += (str(onset[i]) + '\t')
    outString += str(RT[i])
    outfile.write(outString + '\n')

outfile.close()

