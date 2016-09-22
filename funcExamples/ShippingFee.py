def ShippingRate(spending, nonProfit='n'):
    if nonProfit == 'y':
        if spending < 50:
            fee = 3
        elif spending < 100:
            fee = 6
        elif spending < 150:
            fee = 9
        else:
            fee = spending * 0.06
    else:
        fee = spending * 0.08
    return fee
