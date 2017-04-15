import configparser
config = configparser.ConfigParser()
config.read('config.ini')

def read(value):
    return config['DEFAULT'][value]
