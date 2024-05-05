#Q1 
# only_consonants takes a string and returns only consonants
def only_consonants(s):

    vowels = ('a', 'e', 'o', 'u', 'i', 'y')
    
    s = s.lower() # ensures that letters in the input string are lower case
    consonants = ''

    # goes through every letter in s and adds consonants to consonants object
    for l in s:
        if l not in vowels:
            consonants += l
    return consonants


print(only_consonants('name'))


#Q2 
# Takes a string and capitalise the letters according to english grammar rules
def capitalise(s):
    capitalised = ''
    for i in range(len(s)):

        # The first letter of a string is capitalised
        if i == 0:
            capitalised += s[0].upper()

        # checks if a letter is the first letter in a new sentence
        elif i > 2 and s[i-2] in ['?', '!', '.']:
            capitalised += s[i].upper()

        # capitalise the word I
        elif (s[i] == 'i') and (s[i-1] == ' ') and (s[i+1] == ' '):
            capitalised += s[i].upper()

        else:
            capitalised += s[i]
    
    return capitalised


print(capitalise('hello, how are you?'))


#Q3 scrabble_score takes a string and calculates how much points a player gets 
def scrabble_score(s):
    score = 0
    one = ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']
    two = ['d', 'g']
    three = ['b', 'c', 'm', 'p']
    four = ['f', 'h', 'v', 'w', 'y']
    five = ['k']
    eight = ['j', 'x']
    ten = ['q', 'z']
    for letter in s:
        if letter in one:
            score += 1  
        elif letter in two:
            score += 2 
        elif letter in three:
            score += 3 
        elif letter in four:
            score += 4
        elif letter in five:
            score += 5 
        elif letter in eight:
            score += 8 
        elif letter in ten:
            score += 10
    return score

print(scrabble_score('right'))  

#Q4
# low_high_removed removes r number of lowest and highest numbers in a list
def low_high_removed(n, r):
    sorted_n = sorted(n)
    return sorted_n[r:-r]

print(low_high_removed([1, 8,11,77,99,44,665,48, 5, 8, 97], 2))

#Q5
# perfect checks if a number is perfect
def perfect(n):
    total = 0
    for i in range(1,int(n/2+1)):
        if n % i == 0:
            total += i
    if total == n:
        return True
    else:
        return False

print(perfect(29))

