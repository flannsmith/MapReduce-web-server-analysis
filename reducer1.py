#!/usr/bin/env python

import sys 
import os

""" Processes the csv file created by mapper by and returns the total number of 
of connections to the server i.e. total server entries """

def reducer1():
    count = 0
    for line in sys.stdin:

    # fd = os.open(sys.argv[1], os.O_RDWR)
    # ret = os.read(fd, 1000000).decode('utf-8')
    #sums no. of entries in csv file created by mapper
        count +=1
    return count

if __name__ == "__main__":
    print(reducer1())


