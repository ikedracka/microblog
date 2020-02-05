# it's better to store config details separately from the app code

import os

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'my-secret-key'  #gets the value of 'SECRET_KEY' environment variable