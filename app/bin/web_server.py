#!/usr/bin/env python
from bottle import route, run

@route('/<endpoint>')
def hello(endpoint):
    return "Hello World! You have reached: {0}\n".format(endpoint)

@route('/<endpoint>/<a>')
def hello(endpoint, a):
    return "Hello World! You have reached: {0}/{1}\n".format(endpoint, a)

@route('/<endpoint>/<a>/<b>')
def hello(endpoint, a, b):
    return "Hello World! You have reached: {0}/{1}/{2}\n".format(endpoint, a, b)

@route('/<endpoint>/<a>/<b>/<c>')
def hello(endpoint, a):
    return "Hello World! You have reached: {0}/{1}/{2}/{3}\n".format(endpoint, a, b, c)

@route('/<endpoint>/<a>/<b>/<c>/<d>')
def hello(endpoint, a):
    return "Hello World! You have reached: {0}/{1}/{2}/{3}/{4}\n".format(endpoint, a, b, c, d)


run(host='0.0.0.0', port=8080, server='paste', debug=True)
