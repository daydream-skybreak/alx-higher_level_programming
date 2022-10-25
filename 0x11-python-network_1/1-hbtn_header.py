#!/usr/bin/python3
""" 
sends a request to the URL and displays the value of the X-Request-Id variable
"""
if __name__ == '__main__':
    import urllib.request
    from sys import argv

    arg = argv[1]

    request = urllib.request.Request(arg)
    with urllib.request.urlopen(request) as res:
        print(dict(res.headers).get('X-Request-Id'))
