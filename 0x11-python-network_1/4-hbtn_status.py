#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests
    r = requests.get('http://0.0.0.0:5050/status')
    t = r.reason
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(t), t))
