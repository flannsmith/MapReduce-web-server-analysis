#!/usr/bin/env python

import sys
import os

""" Processes the csv file created by mapper by and returns the distinct 
number of IPs  """

count = 0
unique_IPs = set(content)
for entry in unique_IPs:
    count+=1
return count
