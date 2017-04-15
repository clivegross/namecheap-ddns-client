import sys
import time
from util import *
import config

UPDATE_INTERVAL = 600
public_ip = 'N/A'

def get_public_ip():
    return get('ifconfig.io', '/ip').read().decode().rstrip()

def update_succesfull(res):
    return res.status == 200 and '<ErrCount>0</ErrCount>' in res.read().decode()

def update_ddns():
    params = [
        '?host=' + config.read('host'),
        '&domain=' + config.read('domain'),
        '&password=' + config.read('ddns_password')
    ]
    res = get('dynamicdns.park-your-domain.com', '/update' + ''.join(params))
    if update_succesfull(res):
        print('Succesfully updated DNS.')
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
    time.sleep(UPDATE_INTERVAL)
