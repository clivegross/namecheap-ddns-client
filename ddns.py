#!/usr/bin/python3
# File name: ddn.py
# Description: Updates a Namecheap Dynamic DNS record with the hosts public IP address, obtained from checkip.amazonaws.com.
# Author: Clive Gross
# Last updated: 20-06-2023

import time
from util import get_public_ip, update_ddns
import config


def main():
    public_ip = 'N/A'
    host = config.read('HOST')
    domain = config.read('DOMAIN')
    password = config.read('DDNS_PASSWORD')

    while True:
        current_ip = get_public_ip()
        if public_ip != current_ip:
            print('Public IP Changed from ' + public_ip + ' to ' + current_ip + '.')
            if update_ddns(host, domain, password, current_ip):
                public_ip = current_ip
        time.sleep(config.read('UPDATE_INTERVAL', int))


if __name__ == '__main__':
    main()
