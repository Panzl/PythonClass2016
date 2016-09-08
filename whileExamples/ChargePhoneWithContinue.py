charge = 18    #initial charge

while True:
    charge += 3   # the phone is charged 3% during this period
    if charge < 90:
        continue
    if charge >= 100:
        break
    print('Your phone is ' + str(charge) + '% charged')

# message that the phone is fully charged
print('Fully charged!')
