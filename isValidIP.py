import ipaddress
import re
import os

def valid_ip(address):
    try:
        print(ipaddress.ip_address(address))
        return True
    except:
        return False


access_log = os.path.abspath("access_log")
ret = os.read(access_log, 756899).decode('utf-8')



#pattern = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
pattern = r"^.{3}$"
pattern_re = re.compile(pattern)
Ip_addr = pattern_re.findall(ret)


print(Ip_addr)

