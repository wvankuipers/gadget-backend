import os

VERSION = '1.0.0'
DEV_MODE = os.getenv('DEV_MODE', False)
SECRET_KEY = 'secret' # Change in production