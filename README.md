# MapReduce web server analysis
## Cloud computing 41110 assignment 
A common task in digital forensics is the analysis of log files.  
Each line (entry) of a web server’s log file normally contains important information such as IP addresses, date and time of request, request line, HTTP status, etc.
This program takes a log file as an input (access_log) and then extracts the following information from the log files:  
the total number of connections to the server(i.e.  total numbers of entries), the number of distinct IPs and the number of entries for each IP. 

## Run the code from the command line

```
./mapper.py | sort | ./reducer1.py
```

```
./mapper.py | sort | ./reducer2.py
```

```
./mapper.py | sort | ./reducer3.py
```
