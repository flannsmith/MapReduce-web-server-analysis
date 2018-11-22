#!/usr/bin/env python
import os
import sys
import ipaddress
import re
import csv
import operator

# access_log = os.path('/Users/lindasmith/Desktop/DTOP/MSC/Semester3/cloudComputing'+'access_log')
access_log = os.path.abspath("access_log")

mapped_log = os.path.abspath("IPs_sorted_mapped.csv")

def mapper(log_file):

    fd = os.open(log_file, os.O_RDWR)
    ret = os.read(fd, 756899).decode('utf-8')
    pattern = r"\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    pattern_re = re.compile(pattern)
    Ip_addr = pattern_re.findall(ret)
    for IP in Ip_addr:
        result = (IP + "\t" + "\t" + "1" + "\n")
        with open('IPs_mapped.csv', 'a') as f:
            f.write(result)
    return result


def reducer(csv_file_path):
    kv_dict = {}
    for line in csv_file_path:
        word, count = line.split()
        if word in kv_dict.keys():
            kv_dict[word] += int(count)
        else:
            kv_dict[word] =1
    for word in kv_dict.keys():
        print(word, kv_dict[word])



#Reducer to count total number of server connections
def reduce_Server_Conn(csv_file_path):
    #sums no. of IPs in validIPs csv file
    IP_count = sum(1 for row in csv_file_path)
    return IP_count

#Reducer to count number of distinct IPs
def reduce_Unique_IPs(csv_file_path):
    #sums no. of IPs in validIPs csv file
    IP_count = sum(1 for row in csv_file_path)
    return IP_count
    

#Reducer to count no. of entries for each IP
def entries_per_IP(csv_file_path):
    pass


if __name__ == "__main__":
    print(mapper(access_log))

    # print(reducer(mapped_log))




    #numConnections = reduce_Server_Conn('/Users/lindasmith/Desktop/DTOP/MSC/Semester3/cloudComputing/IPs_mapped.csv')
    #print('Total no. connections to server: ', numConnections)
    #numUniqueIPs = (reduce_Unique_IPs('/Users/lindasmith/Desktop/DTOP/MSC/Semester3/cloudComputing/IPs_mapped.csv'))
    # print("Unique no. of IPs in server log: ", numUniqueIPs)
 

