#!/usr/bin/python3
# File name: ddn.py
# Description: Updates a Namecheap Dynamic DNS record with the hosts primary local IP address (private IP address), not its public IP address.
# Use this version for a host you wish to reach from within a private intranet.
# Note the host must have outgoing internet access to reach dynamicdns.park-your-domain.com.
# Author: Clive Gross
# Last updated: 20-06-2023

import time
from util import get_private_ip, update_ddns
import config


def main():
    private_ip = 'N/A'
    host = config.read('HOST')
    domain = config.read('DOMAIN')
    password = config.read('DDNS_PASSWORD')
    
    while True:
        current_ip = get_private_ip()
        if private_ip != current_ip:
            print('Primary local IP Changed from ' + private_ip + ' to ' + current_ip + '.')
            if update_ddns(host, domain, password, current_ip):
                private_ip = current_ip
        time.sleep(config.read('UPDATE_INTERVAL', int))


if __name__ == '__main__':
    main()
