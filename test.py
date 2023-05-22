#!/usr/bin/python3
import sys
import time
from util import *
import config

UPDATE_INTERVAL = 600
public_ip = 'N/A'

def get_public_ip():
    return get('checkip.amazonaws.com', '/').read().decode().rstrip()

def update_succesfull(res):
    print(res.read().decode(), file=sys.stderr)
    return res.status == 200 and '<ErrCount>0</ErrCount>' in res.read().decode()

def update_ddns():
    params = [
        '?host=' + config.read('host'),
        '&domain=' + config.read('domain'),
        '&password=' + config.read('ddns_password'),
        '&ip=' + get_public_ip()
    ]
    path = '/update' + ''.join(params)
    print(path, file=sys.stderr)
    res = get('dynamicdns.park-your-domain.com', path)
    if update_succesfull(res):
        print('Succesfully updated DNS.')
        return True
    else:
        print('DNS update failed.', file=sys.stderr)
        return False

# https://dynamicdns.park-your-domain.com/update?host=[host]&domain=[domain_name]&password=[ddns_password]&ip=[your_ip]

update_ddns()