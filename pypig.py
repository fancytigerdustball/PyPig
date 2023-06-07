''' PyPig '''

def _get_words(text):
    ''' Returns the words in the text '''

    chars = sorted(set(text))
    notalpha = [' ']

    # Find non-alphabetical text
    for c in chars:
        if not c.isalpha():
            notalpha.append(c)
    notalpha = list(set(notalpha))

    # Split sentences into words by non-alpha characters
    words = text
    for c in notalpha:
        words = words.replace(c, '_')
    words = words.lower().split('_')
    while '' in words:
        words.remove('')   

    return words

def pigify(text):
    ''' Returns text argument in pig latin '''

    words = _get_words(text)

    platin = ''
    for word in words:
        first = word[0]
        word = word[1:] + first + 'ay'
        platin += word + ' '

    return platin

def depigify(platin):
    ''' Returns the pig latin in English '''

    words = _get_words(platin)

    english = ''
    for word in words:
        word = word[:-2] # Without "ay"
        word = word[-1] + word
        word = word[:-1] # Chop off the last letter
        english += word + ' '

    return english
