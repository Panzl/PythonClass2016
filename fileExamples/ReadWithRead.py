import os

# changing the working directory to the appropriate directory
WorkDir = 'TestData'  #this needs to be customized
os.chdir(WorkDir)

# first, open the file
f = open('MultiLineData.txt', 'r')
# read the entire file content into a string variable fileData
fileData = f.read()
# always close the file you opened
f.close()
