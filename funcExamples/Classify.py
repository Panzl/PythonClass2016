def Classify(rating):
    if rating >= 90:
        outcome = 'Excellent'
    elif rating >= 80:
        outcome = 'Good'
    elif rating >= 65:
        outcome = 'Fair'
    else:
        outcome = 'Poor'
    return outcome

