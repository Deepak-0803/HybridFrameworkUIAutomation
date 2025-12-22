from configparser import ConfigParser


def read_configuration(category,key):
    config = ConfigParser()
    config.read("configuration/config.ini")
    config.get(category,key)
    return config.get(category,key)