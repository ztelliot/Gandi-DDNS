"""Gandi DDNS v1.0 By Elliot"""
import requests
import json
import re

with open('config.json', 'r') as rf:
    config = rf.read()
config = eval(config)
rf.close()

api_key = config['api_key']
headers = {
    'X-Api-Key': api_key,
    'Content-Type': 'application/json'
}

def get_ip(type):
    if type == 'AAAA':
        ipify = '6'
        type = '6'
        name = 'ipv6'
    else:
        ipify = ''
        type = '4'
        name = 'ipv4'
    url = ['', 'https://api-ipv' + type + '.ip.sb/jsonip', 'https://api' + ipify + '.ipify.org?format=json', 'http://ip' + type + 'only.me/api/']
    try:
        for i in [1, 2, 3]:
            url = url[i]
            if i in [1, 2]:
                ip = requests.get(url).json()['ip']
            else:
                ip = requests.get(url).text
                ip = re.findall(r",(.+?),", ip)[0]
            print('Your ' + name + ' is:', ip)
            return ip
    except:
        print('Get ' + name + ' Address Error!')
        return 0

def get_dns(url):
    try:
        result = requests.get(url, headers=headers).json()
        result = result['rrset_values'][0]
        return result
    except:
        return 0

def add_dns(url):
    try:
        result = requests.post(url, headers=headers, data=data).json()['message']
        if result == 'DNS Record Created':
            print('Creat ' + record + '.' + domain + ' ' + type + ' Record Succeed!')
        else:
            print(result)
    except:
        print('Unknown Error!')

if __name__ == '__main__':
    try:
        ipv4 = get_ip("A")
        ipv6 = get_ip("AAAA")
        for domain in config['domain']:
            records = config['domain'][domain]
            for record in records:
                for type in records[record]:
                    if type == 'A':
                        ip = ipv4
                    elif type == 'AAAA':
                        ip = ipv6
                    else:
                        print(type + ' is an Unsupported DNS Type!')
                        break
                    if ip == 0:
                        print("Can't Refresh " + record + '.' + domain + ' ' + type + ' Record!')
                        break
                    url = 'https://dns.api.gandi.net/api/v5/domains/' + domain + '/records/' + record + '/' + type
                    data = json.dumps({"rrset_type": type, "rrset_ttl": 300, "rrset_values": [ip]})
                    old_ip = get_dns(url)
                    if old_ip == ip:
                        print(record + '.' + domain + ' ' + type + " Record Don't Need refresh!")
                    elif old_ip == 0:
                        add_dns(url)
                    else:
                        try:
                            result = requests.put(url, headers=headers, data=data).json()['message']
                            if result == 'DNS Record Created':
                                print('Refresh ' + record + '.' + domain + ' ' + type + ' Record Succeed!')
                            else:
                                print(result)
                        except:
                            print('Refresh ' + record + '.' + domain + ' ' + type + ' Record Failed!')
    except:
        print('Something Wrong!')
