import operator
from operator import itemgetter
import sys

content = open('IPs_mapped.csv', "r").readlines()

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in content:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print ('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print ('%s\t%s' % (current_word, current_count))




















# previous = None
# sum = 0
# for line in sys.stdin:
#     key, value = line.split('\t',1)
   
#     if key != previous:
#         if previous is not None:
#             print(str(sum) + '\t' + previous)
#         previous = key
#         sum = 0

#     sum = sum + int(value)
# print(str(sum) + '\t' + previous)



#Reducer to count number of server connections
# def server_connections(content):
#     #sums no. of IPs in validIPs csv file
#     IP_count = sum(1 for row in content)
#     return IP_count   


# #Reducer to count number of distinct IPs
# #first I need to sort IPs into blocks of occurring entries then find unique
# def unique_IPs(content): 
#     count = 0
#     unique_IPs = set(content)
#     for entry in unique_IPs:
#         count+=1
#     return count

# #Reducer to count no. of entries for each IP
# #Sorts entries by IP
# def Entries_By_IP(content):
#     sorted_IPs = sorted(content, key=operator.itemgetter(1))
#     pass

# print(server_connections(content))
# print(unique_IPs(content))
