#!/usr/bin/env python

import sys
import os

""" Processes the output from the mapper and returns the number of distinct IPs  """

def reducer2():
    IPs = []
    for line in sys.stdin:
        #print(line, end="")
        IPs.append(line)
    
    unique_IPs = set(IPs)
    num_unique_IPs =(len(unique_IPs))
    return num_unique_IPs


if __name__ == "__main__":
    print(reducer2())


