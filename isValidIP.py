def valid_ip(address):
    try:
        print(ipaddress.ip_address(address))
        return True
    except:
        return False
