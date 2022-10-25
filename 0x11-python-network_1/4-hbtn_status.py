#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    t = r.reason
    print("Body response:\n\t- type: {}\n\t- body: {}".format(type(t), t))
