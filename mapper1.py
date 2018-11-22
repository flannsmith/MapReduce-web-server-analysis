#!/usr/bin/env python
import os
import sys
import ipaddress
import re
import csv
import operator


#Takes access_log as input from command line and returns all IP addresses with the number of their occurrence
#How many bytes can a mapreduce read in maximum
list_ip = []
fd = os.open(sys.argv[1], os.O_RDWR)
ret = os.read(fd, 1000000).decode('utf-8')
# print(ret)
# pattern = r"\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
pattern = re.compile(r'(?<=\n)(\d+\.\d+\.\d+\.\d+)(?=\s)')
pattern_2 = re.compile(r'(^\d+\.\d+\.\d+\.\d+)')
list_ip = pattern.findall(ret)
list_first_ip = pattern_2.findall(ret)
list_ip += list_first_ip
# space_ips_end = pattern_2.findall(ret)
# print(len(list_ip - space_ips_end))
print(list_ip)
print(len(list_ip))
# pattern_re = re.compile(pattern)
# Ip_addr = pattern_re.findall(ret)
# for IP in Ip_addr:
#         result = (IP + "\t" + "\t" + "1")
#         print(result)
#         with open('IPs_mapped.csv', 'a') as f:
#                 f.write(result)


