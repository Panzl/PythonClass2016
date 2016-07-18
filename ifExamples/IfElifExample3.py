age = 56
bpMed = 'no'
BMI = 31
if age>=65:
    # meeting the criterion 1
    print('You meet the criterion 1')
    print('You are eligible to parcipate in the study')
elif (age>=55) and (bpMed=='yes'):
    # meeting the criterion 2
    print('You meet the criterion 2')
    print('You are eligible to parcipate in the study')
elif (age>=50) and (age<=59) and (BMI>30):
    # meeting the criterion 3
    print('You meet the criterion 3')
    print('You are eligible to parcipate in the study')
else:
    print('You did not meet the criteria')
    print('You are ineligible to parcipate in the study')

