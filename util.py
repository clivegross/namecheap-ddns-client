#!/usr/bin/python3
import http.client

def get(url, path):
    connection = http.client.HTTPSConnection(url)
    connection.request('GET', path)
    response = connection.getresponse()
    return response