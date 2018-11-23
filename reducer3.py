#!/usr/bin/env python

import sys
import os

""" Receives and processes the mappers output (stdout) and returns the total number of 
of entries for each IP in the server log """

def reducer3():

    IP_dict = {}
    
    # input comes from STDIN
    for line in sys.stdin:
        word, count = line.split('\t\t')
        if word not in IP_dict.keys():
            IP_dict[word] = int(count)
        else:
            IP_dict[word] += int(count)
            
    for k, v in IP_dict.items():
        print(k, v)

if __name__ == "__main__":
    reducer3()
