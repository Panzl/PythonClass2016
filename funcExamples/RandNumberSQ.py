import random

def randsq(size):
    for i in range(size):
        for j in range(size):
            print(random.randint(0,9), end='')
        print()
