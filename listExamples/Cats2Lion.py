mammal = ['cat', 'dog', 'cat', 'cat', 'tiger']
while 'cat' in mammal:
    indCat = mammal.index('cat')
    mammal[indCat] = 'lion'
    #mammal.insert(indCat,'lion')
    #mammal.remove('cat')
