import os
from bottle import route, static_file

@route('/')
def index():
    dirname = os.path.dirname(os.path.realpath(__file__))
    return static_file('fresh_tomatoes.html', dirname)
