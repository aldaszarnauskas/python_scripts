#Q1
# head displays the first ten lines of a text
def head(fname):
    with open(fname, 'r') as fname:
        for n in range(10):
            print(fname.readline())

print(head('fines.txt'))

#Q2
# head2 writes the first ten lines while adding head_ in the begining of each line
def head2(fname):

    head = []

    with open(fname, 'r') as fname1:
        for i in range(10):
            head.append(fname1.readline())
    
    with open(f'head_{fname}', 'w') as fname2:
        fname2.writelines(head)

#Q3
# word_length calculates the average word length in a file
def word_length(fname):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'y', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'r', 's', 't', 'q', 'u', 'x', 'v', 'w', 'z']

    with open(fname, 'r') as fname1:
        
        count = 0
        total = 0


        for line in fname1:
            count += 1
            words = ''

            # Goes through each symbol in a line and adds letters to words. If encountered symbol
            # is not a letter, then, the dot is added to words so that dot symbol would be specified
            # to split words object
            for letter in line:
                if letter.lower() in alpha:
                    words += letter
                else:
                    words += '.'
            
            split_words = words.split('.')
            
            # Calculates the number of letters across all words
            total_words_length = 0
            for word in split_words:
                total_words_length += len(word)
            
            # calculates the average number of letters across all words
            avg_words_length = total_words_length / (len(split_words)-1)
            total += avg_words_length

        # calculates the average word length across all lines
        word_length = total / count

        return word_length