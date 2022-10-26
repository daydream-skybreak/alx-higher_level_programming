#!/usr/bin/python3
"""
takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
displays the body of the response
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    url = argv[1]
    email = {'email': argv[2]}
    value = urllib.parse.urlencode(email).encode('ascii')
    request = urllib.request.Request(url, value)

    with urllib.request.urlopen(request) as res:
        print(res.read().decode('utf-8'))
