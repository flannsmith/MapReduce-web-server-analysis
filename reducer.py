import operator

content = open('IP_input.csv', "r").readlines()

#Reducer to count number of server connections
def server_connections(content):
    #sums no. of IPs in validIPs csv file
    IP_count = sum(1 for row in content)
    return IP_count   


#Reducer to count number of distinct IPs
#first I need to sort IPs into blocks of occurring entries then find unique
def unique_IPs(content): 
    count = 0
    unique_IPs = set(content)
    for entry in unique_IPs:
        count+=1
    return count

#Reducer to count no. of entries for each IP
#Sorts entries by IP
def Entries_By_IP(content):
    sorted_IPs = sorted(content, key=operator.itemgetter(1))
    pass

print(server_connections(content))
print(unique_IPs(content))
