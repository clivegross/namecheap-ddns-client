import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def read(value, type=str):
    if type==str:
        return config['DEFAULT'][value]
    elif type==int:
        return config['DEFAULT'].getint(value)
    else:
        return config['DEFAULT'][value]
