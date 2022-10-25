#!/usr/bin/python3
"""
sends a request to a url and displays the value of the variable 'X-Request-Id'
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
