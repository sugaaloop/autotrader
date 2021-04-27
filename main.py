# Python 3 server example
# from http.server import BaseHTTPRequestHandler, HTTPServer
# import time

import hug

from autotrader import quoteCtrl as quote
from autotrader import entityRepo

@hug.extend_api('/quote')
def quote_api():
    return [quote]

@hug.get('/thing')
def thing():
    print('thing')
    return 'thing'

@hug.get('/')
def home():
    print('home')
    return 'home'
