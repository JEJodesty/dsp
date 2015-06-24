#!/usr/bin/env python

"""
Description:
This code contains some funtions adapted from markov.py by Allen B. Downey.
http://www.greenteapress.com/thinkpython/code/markov.py
Date - 6/22/2015

Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import sys
import random
import string

textfile = sys.argv[1]
word_amount = sys.argv[2]

text_file = open(textfile, "r")
word_list = text_file.read().split()
word_list = [x.replace("_", " ") for x in word_list]
word_list = [x.replace("-", " ") for x in word_list]
word_list = [x.strip(string.punctuation + string.whitespace) for x in word_list]
word_list = [x.lower() for x in word_list]
# print lines

suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words
output_words = []

# modding 1

def process_wordlist(wordlist, order=2):
    # word_count = 0
    for word in wordlist:
        process_word(word, order)
        #word_count += 1
    # print word_count
    #print suffix_map

# Copyright 2012 Allen B. Downey
# http://www.greenteapress.com/thinkpython/code/markov.py
def process_word(word, order=2):
    """Processes each word.
    word: string
    order: integer
    Durng the first few iterations, all we do is store up the words;
    after that we start adding entries to the dictionary.
    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]
        
    prefix = shift(prefix, word)

# Copyright 2012 Allen B. Downey
# http://www.greenteapress.com/thinkpython/code/markov.py
def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.
    t: tuple of strings
    word: string
    Returns: tuple of strings
    """
    return t[1:] + (word,)

# Copyright 2012 Allen B. Downey
# http://www.greenteapress.com/thinkpython/code/markov.py
def random_text(n):
    """Generates random wordsfrom the analyzed text.
    Starts with a random prefix from the dictionary.
    n: number of words to generate
    """
    start = random.choice(suffix_map.keys())
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n-i)
            return
        # choose a random suffix
        word = random.choice(suffixes)
        # Jodesty: *Need to learn how to format text output to fit on terminal screen
        output_words.append(word)
        # Jodesty: *what I have for now
        print word,
        start = shift(start, word)

process_wordlist(word_list, 2)
random_text(40)
