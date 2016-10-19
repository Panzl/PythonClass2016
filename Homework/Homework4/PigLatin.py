def PigLatinWord(word):
    vowel = ['a', 'e', 'i', 'o', 'u']
    punct = ['.', ',']

    # checking if the last character is a punctuation mark
    if word[-1] in punct:
        # if a punctuation mark, then save the punctuation mark
        # and drop the last character
        lastChar = word[-1]
        word = word[:-1]
    else:
        # otherwise, we save an empty space
        lastChar = ''
        
    # the first letter is a vowel
    if word[0] in vowel:
        newWord = word + 'yay' + lastChar
    # the first letter is not a vowel
    else:
        # find the first vowel
        iVowel = 1
        while word[iVowel] not in vowel:
            iVowel += 1
        # re-organizing the word
        newWord = word[iVowel:] + word[:iVowel] + 'ay' + lastChar

    # returning the translated word
    return newWord


def PigLatin(text):
    # converting the input into lower case, then spliting into words
    inWords = text.lower().split()
    
    # translating word by word
    outWords = []
    for iWord in inWords:
        outWords.append(PigLatinWord(iWord))
        
    # putting back to a sentence
    outText = ' '.join(outWords)

    # returning the translated sentence
    return outText


TestText1 = 'Her cat, being so startled, ran away into the dark.'
TestText2 = 'May the Schwartz be with you.'


    
