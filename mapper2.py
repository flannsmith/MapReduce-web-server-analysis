#!/usr/bin/env python
import os
import sys
import ipaddress
import re
import csv
import operator

""" Mapper that takes command line input and returns only distinct/unique IPs in access_log file to csv """

#Make a dictionary with all the keys (IPs) in file 

fd = os.open(sys.argv[1], os.O_RDWR)
ret = os.read(fd, 1000000).decode('utf-8')
pattern = r"\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
pattern_re = re.compile(pattern)
Ip_addr = pattern_re.findall(ret)
for IP in Ip_addr:
        result = (IP + "\t" + "\t" + "1" + "\n")
        print(result)
        with open('IPs_mapped.csv', 'a') as f:
                f.write(result)

