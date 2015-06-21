__author__ = 'Joshua'

# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.
    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    count = 0
    for s in words:
        r = len(s) - 1
        if len(s) >= 2:
            if s[0:1] == s[r:]:
                count += 1
    return count

    raise NotImplementedError

# print match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
# print match_ends(['', 'x', 'xy', 'xyx', 'xx'])
# print match_ends(['aaa', 'be', 'abc', 'hello'])
# print ""

def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    newwords = []
    count = 0
    words.sort()
    for s in words:
        if s[0:1] == "x":
            newwords.append(s)
        count += 1
    for i in newwords:
        words.remove(i)
    newwords.extend(words)
    return newwords
    raise NotImplementedError

# print front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
# print front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
# print front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
# print ""

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].
    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    newlist = sorted(tuples, key=lambda x: x[-1])
    return newlist
    raise NotImplementedError

# print sort_last([(1, 3), (3, 2), (2, 1)])
# print sort_last([(2, 3), (1, 2), (3, 1)])
# print sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
# print ""

def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    numlist = nums
    if numlist:
        firstval = numlist[0]
        # find lowest index of value != firstval
        for index, value in enumerate(numlist):
            if value != firstval:
                return [firstval] + remove_adjacent(numlist[index:])
        # no such value found
        return [firstval]
    else:
        # empty list
        return []
    raise NotImplementedError

# print remove_adjacent([1, 2, 2, 3])
# print remove_adjacent([2, 2, 3, 3, 3])
# print remove_adjacent([3, 2, 3, 3, 3])
# print ""

def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.
    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    list1.extend(list2)
    list1.sort()
    return list1
    raise NotImplementedError

# print linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
# print linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
# print linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
