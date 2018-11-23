#!/usr/bin/env python
import os
import sys
import ipaddress
import re
import csv
import operator

"""Takes access_log as input from command line and returns all IP addresses with the number of their occurrence"""
def mapper():

    list_ip = []
    fd = os.open(sys.argv[1], os.O_RDWR)
    #Specify the no. of bytes to read in. Total size of access_log is 756899 bytes 
    ret = os.read(fd, 756899).decode('utf-8')

    #Regex to find new line preceding IP address and find a space after IP 
    pattern = re.compile(r'(?<=\n)(\d+\.\d+\.\d+\.\d+)(?=\s)')
    #Regex finding the first IP address in the whole file
    pattern_2 = re.compile(r'(^\d+\.\d+\.\d+\.\d+)')
    list_ip = pattern.findall(ret)
    list_first_ip = pattern_2.findall(ret)
    #Join both expression patterns to retrieve all IPs- 4224 in total
    list_ip += list_first_ip
    # print(list_ip)
    # print(len(list_ip))
    for IP in list_ip:
            result = ("{}\t\t1\n".format(IP))
            print(result,end="")
            with open('IPs_mapped.csv', 'a') as f:
                    f.write(result)


if __name__ == "__main__":
    mapper()