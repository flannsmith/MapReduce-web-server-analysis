import os, sys
import ipaddress
import re
import csv
import operator


class MapReduce_LogAnalysis:

    def valid_ip(self, address):
        try:
            ipaddress.ip_address(address)
            return True
        except:
            return False

    path = '/Users/lindasmith/Desktop/DTOP/MSC/Semester3/cloudComputing'

#To get file size in bytes 
#print(os.path.getsize('/Users/lindasmith/Desktop/DTOP/MSC/Semester3/cloudComputing/access_log'))

# print(ret)

#RegEx to match IP addresses. Depending on the nature of the file you have 
#this regex will do the job. Be careful as it will match 999.999.999.999
#which is not a valid ip address 

    def mapper(self, access_log):
    #OS.open takes file name and size of file in bytes
    #756899
        
        fd = os.open("access_log", os.O_RDWR)

        ret = os.read(fd, 756899).decode('utf-8')
        pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        pattern_re = re.compile(pattern)
        Ip_addr = pattern_re.findall(ret)

        V = valid_ip()
        for IP in Ip_addr:
            if(V(IP)):
                result = (IP + "\t" + "1" + "\n")
        
        yield()


        #Checks in the IP is valid, writes the output and keys to csv file for reducer 
        for IP in Ip_addr:
            if(valid_ip(IP)):
                result = (IP + "\t" + "1" + "\n")
                with open('IP_input.csv', 'a') as f:
                    f.write(result)






        
#Shuffle - group and sort all intermediate values that have the same output key

#./mapper.py < input.txt | sort
#touch input.txt
#chmod u+x mapper.py











