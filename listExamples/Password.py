passwords = ['aaargh', 'fjfjkdg', 'qwerty']
while True:
    print('Please enter the password')
    userPassword = input()
    if userPassword in passwords:
        break
    else:
        print('Incorrect password!')

print('Access granted!')
