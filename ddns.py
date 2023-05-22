#!/usr/bin/python3
import sys
import time
from util import *
import config
from xml.etree import ElementTree


public_ip = 'N/A'

def get_public_ip():
    return get('checkip.amazonaws.com', '/').read().decode().rstrip()

def update_successful(res):
    response_string = res.read().decode().rstrip()
    error_count = int(ElementTree.fromstring(response_string).find("ErrCount").text)
    return res.status == 200 and error_count == 0

def update_ddns():
    # https://dynamicdns.park-your-domain.com/update?host=[host]&domain=[domain_name]&password=[ddns_password]&ip=[your_ip]
    params = [
        '?host=' + config.read('HOST'),
        '&domain=' + config.read('DOMAIN'),
        '&password=' + config.read('DDNS_PASSWORD'),
        '&ip=' + get_public_ip()
    ]
    path = '/update' + ''.join(params)
    res = get('dynamicdns.park-your-domain.com', path)
    if update_successful(res):
        print('Successfully updated DNS.', file=sys.stderr)
        return True
    else:
        print('DNS update failed.', file=sys.stderr)
        return False

while True:
    current_ip = get_public_ip()
    if public_ip != current_ip:
        print('Public IP Changed from ' + public_ip + ' to ' + current_ip + '.')
        if update_ddns():
            public_ip = current_ip
    time.sleep(config.read('UPDATE_INTERVAL', int))
