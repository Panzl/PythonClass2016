charge = 16    #initial charge

while True:
    print('Your phone is ' + str(charge) + '% charged')
    charge += 3   # the phone is charged 3% during this period
    if charge >= 100:
        break

# message that the phone is fully charged
print('Fully charged!')
