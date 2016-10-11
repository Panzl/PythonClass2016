
f = open('TestData/ExerciseData_OneLine.txt')
line = f.readline()
f.close()

inString = line.strip().split()
inNumber = [int(i) for i in inString]
trial = inNumber[:3]
onsetTime = inNumber[3:6]
respTime = inNumber[6:9]
score = inNumber[9:]



