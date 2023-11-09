# 파일읽고 ip주소만 추출하여 분류하는 프로그램

import re
from geolite2 import geolite2


def get_location(ip):
    reader = geolite2.reader()
    location = reader.get(ip)
    geolite2.close()
    return location

ip_list = []
ip_txt = {}
with open('block_ip.txt', 'r') as file:
    for line in file:
        ip_pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
        ip_addresses = re.findall(ip_pattern, line)
        for ip in ip_addresses:
            if ip in ip_list:
                continue
            else:
                ip_list.append(ip)

with open('json.log', 'r') as file:
    for line in file:

        ip_pattern = r'(?<="log":")[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
        ip_addresses = re.findall(ip_pattern, line)
            
        for ip in ip_addresses:
            if ip in ip_list:
                continue
            else:
                ip_list.append(ip)

            location = get_location(ip)
            if location is not None:
                if location["country"]["names"]["en"] == 'Republic of Korea':
                    continue
                ip_txt.update({ip : location["country"]["names"]["en"]})
            else:
                ip_txt.update({ip : 'could not be determined'})

ip_txt = dict(sorted(ip_txt.items(), key=lambda x: x[1]))
with open('ip_list.txt', 'w') as file:
    for key, value in ip_txt.items():
        file.write(f'{key} : {value}\n')

with open('ip_command.txt','w') as file:
    for key, value in ip_txt.items():
        if value != 'Republic of Korea':
            file.write(f'iptables -A INPUT -s {key} -j DROP\n')


with open('all_ip_command.txt','w') as file:
    for ip in ip_list:
        if value != 'Republic of Korea':
            file.write(f'iptables -A INPUT -s {ip} -j DROP\n')