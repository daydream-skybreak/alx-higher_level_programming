#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
manages urllib.error.HTTPError
prints a message 'Error message: {HTTP status code}' 
"""
if __name__ == '__main__':
    import urllib.request
    from sys import argv
    from urllib.error import HTTPError

    try:
        with urllib.request.urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as er:
        print("Error code: {}".format(er.code))