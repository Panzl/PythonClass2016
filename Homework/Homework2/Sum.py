sumInt = 0
sumOdd = 0
sumEven = 0
for i in range(1,101):
    sumInt += i
for j in range(1,101,2):
    sumOdd += j
for k in range(2, 101,2):
    sumEven += k

print('Sum of integers: ' + str(sumInt))
print('Sum of odd numbers: ' + str(sumOdd))
print('Sum of even numbers: ' + str(sumEven))
