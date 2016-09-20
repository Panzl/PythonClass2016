import random

while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print('Outcome = (' + str(dice1) + ', ' + str(dice2) + ')')
    if dice1==1 and dice2==1:
        break

