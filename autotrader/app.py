# hug bootstrap
import os

import hug

from autotrader import controller

def run():
    print('hug server ready', os.environ.get('ACCESS_TOKEN'))


@hug.extend_api('/quote')
def quote_api():
    return [controller]

@hug.get('/thing')
def thing():
    print('thing')
    return 'thing'

@hug.get('/')
def home():
    print('home')
    return 'home'
