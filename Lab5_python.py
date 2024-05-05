#Q1
# to_english takes at maximum three digit number and returns its form in written english
def to_english(n):

    hundreds = ['One hundred', 'Two hundred', 'Three hundred', 'Four hundred', 
    'Five hundred', 'Six hundred', 'Seven hundred', 'Eight hundred', 'Nine hundred']
    tens = ['', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy',
    'eighty', 'ninety']
    tens1 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fithteen', 'sixteen',
    'seventeen', 'eighteen', 'nineteen', 'ten']
    ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    to_english = []
    n = str(n)

    # the condition returns the english written form of a three digit number
    if len(n) == 3:
        if n[1] != '1':
            to_english = hundreds[int(n[0])] + ' ' + tens[int(n[1])] + ' ' + ones[int(n[2])]
        else:
            if n[2] != '0':
                to_english = hundreds[int(n[0])] + ' ' + tens1[int(n[1])]
            else:
                to_english = hundreds[int(n[0])] + ' ' + tens1[9]

    # the condition returns the english written form of a two digit number
    elif len(n) == '2':
        if n[0] != '1':
            to_english = tens[int(n[1])] + ' ' + ones[int(n[2])]
        else:
            if n[1] != '0':
                to_english = hundreds[int(n[0])] + ' ' + tens1[int(n[1])]
            else:
                to_english = hundreds[int(n[0])] + ' ' + tens1[9]

    # the condition returns the english written form of a one digit number
    else:
        to_english = ones[int(n[0])]

    return to_english

print(to_english(110))

#Q2
# is_palindrome checks if a sequence is a palindrome
def is_palindrome(s):
    
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'y', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'r', 's', 't', 'q', 'u', 'x', 'v', 'w', 'z']
    
    s = s.lower()

    # this block puts all letters of a string into a list while excluding spaces and punctuation 
    split_s = []
    for l in s:
        if l in alpha:
            split_s.append(l)
    
    count = 0
    ispalindrome = True
    for l in split_s:
        count += 1
        if l == split_s[-count]:
            ispalindrome = True
        else:
            ispalindrome = False
            break
    return ispalindrome

print(is_palindrome("Doc, note: I dissent. A fast never prevents a fatness. I diet on cod"))

#Q3
# higher_than_prev takes a list of numbers and makes a new list while adding numbers from the first list
# if they are higher the the number before it. The first digit is added to a new list by default.
def higher_than_prev(numlist):


    new_numlist = []

    # it makes the default prev value always be lower by one so that the first digit in a list would be
    # added to a new_numlist in a subsequent for loop
    prev = numlist[0] - 1

    for n in numlist:
        if n > prev:
            new_numlist.append(n)
        prev = n
    
    return new_numlist

print(higher_than_prev([3,3,3,87,631,9,1,89,661,9,9,183,81,31,8,188,132,6]))