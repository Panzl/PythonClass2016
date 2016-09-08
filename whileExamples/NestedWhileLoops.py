while True:
  print('Who are you?')
  name = input()
  if name == 'Joe':
    while True:
      print('Hello, Joe. What is the password? (It is a fish.)') 
      password = input()
      if password == 'swordfish':
        break   # break from the inner while loop
    break   # break from the outer while loop
  
print('Access granted.')

