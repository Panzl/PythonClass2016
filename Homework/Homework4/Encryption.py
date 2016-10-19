def cipher(text):
    # first, create a dictionary
    alphaOrig = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphaCipher = 'TDLOFAGJKRICVPWUXYBEZQSNMH'
    dictCipher = {}
    for i, letter in enumerate(alphaOrig):
        dictCipher[letter] = alphaCipher[i]
        
    # adding space and punctuation marks to the dictionary
    dictCipher[','] = ','
    dictCipher[' '] = ' '
    dictCipher['.'] = '.'

    # encrypting the input text
    inText = text.upper()
    outText = ''
    for iLetter in inText:
        outText += dictCipher[iLetter]

    return outText

phrase = 'Her cat, although being very old, is very agile.'
encripted = cipher(phrase)
print(encripted)
