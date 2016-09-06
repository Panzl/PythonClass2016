initBalance = 500
withdraw = int(input('How much do you want to withdraw? '))
if (withdraw % 10)==0 and withdraw<initBalance:
    print('Your money is available below.')
    newBalance = initBalance - withdraw
    print('Your new balance is $' + str(newBalance) + '.')
else:
    print('Invalid entry')

