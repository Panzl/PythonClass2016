spending = float(input('How much money did you spend? '))
if spending<50:
    shippingFee = 12
elif spending<100:
    shippingFee = 8
elif spending<150:
    shippingFee = 5
else:
    shippingFee = 0

print('Your shipping fee is $' + str(shippingFee) +'.')
