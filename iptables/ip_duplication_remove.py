import re

ip_list = []
with open('block_ip.txt', 'r') as file:
    for line in file:

        ip_pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
        ip_addresses = re.findall(ip_pattern, line)
            
        for ip in ip_addresses:
            if ip in ip_list:
                print(ip)
            ip_list.append(ip)

print(len(list(set(ip_list))))