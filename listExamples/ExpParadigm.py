subjectID = ['001', '003', '004', '006', '009', '012']
expCode = [0, 1, 0, 2, 3, 2]
expParadigm = ['congruent', 'incongruent', 'mixed', 'null']

for i, iSubj in enumerate(subjectID):
    print('Subject ID: ' + iSubj + '    Paradigm: ' + expParadigm[expCode[i]])

