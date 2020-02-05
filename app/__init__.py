from flask import Flask
from config import Config
app=Flask(__name__) # __name__ is Python predefined variable - it's set to the name of the module in which it's used
# For all practical purposes, passing __name__ is almost always going to configure Flask in the correct way
# The app variable is defined as an instance of class Flask in the __init__.py script, which makes it a member of the app package.

# Why isn't it declared as separate variable? such as config = app.config.from_object(Config)?
# apparently it applies the config to 'app' variable - flask app instance
app.config.from_object(Config)

#This one actually imports 'app' defined above? But why?
#The routes are the different URLs that the application implements.
# In Flask, handlers for the application routes are written as Python functions, called view functions.
# View functions are mapped to one or more route URLs so that Flask knows what logic to execute when a client requests a given URL.
from app import routes