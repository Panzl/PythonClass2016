print('What is your first name?')
firstName = input()
print('What is your last name?')
lastName = input()
print(lastName.upper() + ', ' + firstName[0].upper() + firstName[1:].lower())
