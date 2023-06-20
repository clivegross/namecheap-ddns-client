#!/usr/bin/python3
import http.client
import sys
import socket
from xml.etree import ElementTree


def get(url, path):
    """Send HTTP request to url using http.client, including path/params and return response."""
    connection = http.client.HTTPSConnection(url)
    connection.request('GET', path)
    response = connection.getresponse()
    return response


def get_public_ip():
    """Return public IP address of host as string, using checkip.amazonaws.com as provider."""
    return get('checkip.amazonaws.com', '/').read().decode().rstrip()


def get_private_ip():
    """Return primary local IP address of host (private IP address) as string, using socket."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    return ip_address


def update_successful(resp):
    """
    Returns boolean success of http response from dynamicdns.park-your-domain.com.
    True if http status code 200 and no 'ErrCount' objects in response body.
    """
    response_string = resp.read().decode().rstrip()
    error_count = int(ElementTree.fromstring(response_string).find("ErrCount").text)
    return resp.status == 200 and error_count == 0


def update_ddns(host='', domain='', password='', ip_address='127.0.0.1'):
    """
    Update Namecheap Dynamic DNS record by sending the following request:
    https://dynamicdns.park-your-domain.com/update?host=[host]&domain=[domain_name]&password=[ddns_password]&ip=[your_ip]
    Return boolean success of request/response.
    """
    params = [
        '?host=' + host,
        '&domain=' + domain,
        '&password=' + password,
        '&ip=' + ip_address
    ]
    path = '/update' + ''.join(params)
    resp = get('dynamicdns.park-your-domain.com', path)
    if update_successful(resp):
        print('Successfully updated DNS IP address to ' + ip_address + '.', file=sys.stderr)
        return True
    else:
        print('DNS update failed.', file=sys.stderr)
        return False
