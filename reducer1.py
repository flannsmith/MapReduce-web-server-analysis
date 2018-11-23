#!/usr/bin/env python

import sys 
import os

""" Processes the std out created by the mapper and returns the total number of 
of connections to the server i.e. total server entries """

def reducer1():
    count = 0
    for line in sys.stdin:

    #sums no. of entries in csv file created by mapper
        count +=1
    return count

if __name__ == "__main__":
    print(reducer1())


