import random

def CompareNum(a, b):
    if a<b:
        print('Too high')
    elif b<a:
        print('Too low')

# generating a random number
target = random.randint(1,10)

while True:
    # ask the user to enter a number
    guess = int(input('What is the number?'))
    if guess == target:
        # correct guess
        print('You got it!')
        break
    else:
        # otherwise, give a hint, then try again
        CompareNum(target, guess)

