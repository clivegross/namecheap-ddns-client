#!/usr/bin/python3
import configparser
import sys

config = configparser.ConfigParser()
config.read('config.ini')

def read(value, type=str):
    if type==str:
        return config['DEFAULT'][value.lower()]
    elif type==int:
        return config['DEFAULT'].getint(value.lower())
    else:
        return config['DEFAULT'][value.lower()]
