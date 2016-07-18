currentBalance = 4000
payment = 250
while currentBalance > 0:
    print('Current balance is $' + str(currentBalance))
    currentBalance = currentBalance - payment

print('Congrats! You paid off the balance!')
