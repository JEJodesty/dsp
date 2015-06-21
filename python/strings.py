__author__ = 'Joshua'

# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

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
    if 0 < count < 10:
        return "Number of donuts: " + str(count)
    elif count >= 10:
        return "Number of donuts: many"
    raise NotImplementedError


# print donuts(4)
# print donuts(9)
# print donuts(10)
# print donuts(99)
# print ""


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
    length = len(s)
    if length > 2:
        return s[0:2] + s[length - 2:length]
    else:
        return ""
    raise NotImplementedError


# print both_ends("spring")
# print both_ends("Hello")
# print both_ends("a")
# print both_ends("xyz")
# print ""

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
    firstLetter = s[0:1]
    for x in [firstLetter]:
        if x in s:
            s = s.replace(x, "*")
    new_s = firstLetter + s[1:]
    return new_s
    raise NotImplementedError

# print fix_start("babble")
# print fix_start("aardvark")
# print fix_start("google")
# print fix_start("donut")
# print ""

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
    mixStr = b[0:2] + a[2:] + " " + a[0:2] + b[2:]
    return mixStr
    raise NotImplementedError
   
# print mix_up('mix', 'pod')
# print mix_up('dog', 'dinner')
# print mix_up('gnash', 'sport')
# print mix_up('pezzy', 'firm')
# print ""

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
    word = s
    if len(word) >= 3:
        if "ing" in word:
            word += "ly"
        else:
            word += "ing"
    return word
    raise NotImplementedError

# print verbing('hail')
# print verbing('swiming')
# print verbing('do')
# print ""

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
    phrase = s
    if phrase.find("not") < phrase.find("bad"):
        limit = phrase.find("not")
        if phrase.find("!") != -1:
            phrase = phrase[0:limit] + "good!"
        else:
            phrase = phrase[0:limit] + "good"
    return phrase
    raise NotImplementedError

# print not_bad('This movie is not so bad')
# print not_bad('This dinner is not that bad!')
# print not_bad('This tea is not hot')
# print not_bad("It's bad yet not")
# print ""

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

    if (len(a) % 2) == 0:
        alimit = len(a) / 2
    else:
        alimit = (len(a) + 1) / 2

    if (len(b) % 2) == 0:
        blimit = len(b) / 2
    else:
        blimit = (len(b) + 1) / 2

    afront = a[0:alimit]
    aback = a[alimit:len(a)]

    bfront = b[0:blimit]
    bback = b[blimit:len(b)]
    return afront + bfront + aback + bback

    raise NotImplementedError

# print front_back('abcd', 'xy')
# print front_back('abcde', 'xyz')
# print front_back('Kitten', 'Donut')
