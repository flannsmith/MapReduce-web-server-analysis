import os
import sys
import ipaddress
import re
import csv
import operator

# access_log = os.path('/Users/lindasmith/Desktop/DTOP/MSC/Semester3/cloudComputing'+'access_log')
access_log = os.path.abspath("access_log")

def mapper(log_file):

    fd = os.open(log_file, os.O_RDWR)
    ret = os.read(fd, 756899).decode('utf-8')
    pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    pattern_re = re.compile(pattern)
    Ip_addr = pattern_re.findall(ret)
    for IP in Ip_addr:
        result = (IP + "\t" + "1" + "\n")
        #Shuffle / sort IPs with same IPs occurring together in blocks
        # sorted_IPs = sorted(result, key=operator.itemgetter(1))
        # print(sorted_IPs)
        with open('IPs_mapped.csv', 'a') as f:
            f.write(result)
    return result


#Reducer to count total number of server connections
def reduce_Server_Conn(content):
    #sums no. of IPs in validIPs csv file
    IP_count = sum(1 for row in content)
    return IP_count

#Reducer to count number of distinct IPs
def reduce_Unique_IPs(csv_file_path):
    #sums no. of IPs in validIPs csv file
    IP_count = sum(1 for row in csv_file_path)
    return IP_count

#Reducer to count no. of entries for each IP


if __name__ == "__main__":
    mapper(access_log)
    numUniqueIPs = (reduce_Unique_IPs('/Users/lindasmith/Desktop/DTOP/MSC/Semester3/cloudComputing/IPs_mapped.csv'))
    print("Unique no. of IPs in server log: ", numUniqueIPs)
 

