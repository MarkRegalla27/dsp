# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

count = raw_input('Enter Number of Donuts: ')
count = int(count)
def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count < 10:
        print 'Number of donuts: ' + str(count)
    if count >= 10:
        print 'Number of donuts: many'
    raise NotImplementedError


s = raw_input('Enter a string: )
def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) < 2:
        print ' '
    else:
        newString = s[0:2] + s[-2:]
        print newString
    raise NotImplementedError

s = raw_input('Enter string: ')
def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    for i in s:
        if counter > 0:
            if s[counter] == s[0]:
                newString = newString + '*'
            else:
                newString = newString + s[counter]
        else:
            newString = s[counter]
        counter += 1
    raise NotImplementedError

a = raw_input('Enter first word: )
b = raw_input('Enter second word: )
def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
        newa = b[0:2] + a[2:]
        newb = a[0:2] + b[2:]
        print newa + ' ' + newb
    raise NotImplementedError

s = raw_input('Enter string: ')
def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    def verbing(s):
        if len(s) >= 3:
            if s[-3:] == 'ing':
                s = s + 'ly'
                print s
            else:
                s = s + 'ing'
                print s
        else:
            print s

    raise NotImplementedError

s = 'This movie is Not that bAd after all'
def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    notIndex = s.lower().find('not'.lower())        #use .lower() to make search for 'not' and 'bad'
    badIndex = s.lower().find('bad'.lower())        #strings case insensitive
    newS = s[:notIndex] + 'good' + s[badIndex + 3:]
    print newS

    raise NotImplementedError

a = 'abcd'
b = 'efghi'
def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    newString = a[:(len(a)/2)+(len(a)%2)] + b[:(len(b)/2)+(len(b)%2)] + a[(len(a)/2)+(len(a)%2):] + b[(len(b)/2)+(len(b)%2):]
    print newString
    raise NotImplementedError
