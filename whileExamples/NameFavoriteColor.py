# first, the name and favorite color
trueName = 'Tim'
favColor = 'blue'

while True:
    print('What is your name?')
    name = input()
    if name != trueName:
        continue
    print('What is your favorite color?')
    color = input()
    if color == favColor:
        break
    print('Sorry, wrong color!')

print('Congrats!')

