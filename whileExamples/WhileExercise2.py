battery = 16
while True:
    if battery >= 100:
        break
    battery = battery + 3
    print('The battery is ' + str(battery) + '% charged')

print('The battery is fully charged!')
