def pig_latin(s):

    vowels = ['a', 'A', 'o', 'O', 'u', 'U', 'i', 'I', 'e', 'E']
    separators = [',', '.', '!', '.']

    to_pigs_latin = ''

    # splits the s into the separate strings if there is an '\n' in between them
    s = s.splitlines()
    lines = [line.split(' ') for line in s]

    # separate the phrase based on the separators
    phrase = []
    for line in lines:
        for word in line:
            for count, letter in enumerate(word):
                if letter in separators:
                    phrase.append(word[:count])
                    phrase.append(word[count:])
                    break
                elif count == len(word)-1:
                    phrase.append(word)
        phrase += '\n'

    
    # tranlaste a phrase into pig latin
    for c, word in enumerate(phrase):
        for count, letter in enumerate(word):
            # words starting with a vowel
            if letter in vowels and count == 0:
                to_pigs_latin += ' ' + word + 'way'
                break
            # words that are separators
            elif letter in separators or letter == '\n':
                to_pigs_latin += word
                break
            # words that starts with a consonant
            else:
                # words that begins with an upper case
                if letter in vowels and word[0].isupper():
                    to_pigs_latin += ' ' +word[count:].capitalize() + word[:count].lower() + 'ay'
                    break
                # words that begins with a lower case
                elif letter in vowels:
                    to_pigs_latin += ' ' +word[count:] + word[:count].lower() + 'ay'
                    break

    return to_pigs_latin[1:]