import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

config.set('App', 'DevMode', '1' if os.getenv('DEV_MODE', False) else '0')

# DEV_MODE = os.getenv('DEV_MODE', False)
