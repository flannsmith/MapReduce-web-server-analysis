#!/usr/bin/env python

import sys
import os

""" Processes the csv file created by mapper by and returns the total number of 
of entries for each IP in the server log """


def reducer3():

    current_word = ""
    current_count = 0
    word = ""
    input_sort = []
    count=0

# # input comes from STDIN
    for line in sys.stdin:
        word, count = line.split('\t\t')
        # convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            continue
        # by key (here: word) before it is passed to the reducer
        if current_word == word:
            current_count += count
        else:
            if current_word:
                # write result to STDOUT
                print('%s\t%s' % (current_word, current_count))
            current_count = count
            current_word = word

# # do not forget to output the last word if needed!
    if current_word == word:
        return('%s\t%s' % (current_word, current_count))

if __name__ == "__main__":
    print(reducer3())
