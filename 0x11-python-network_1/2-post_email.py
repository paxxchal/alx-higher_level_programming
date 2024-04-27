#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import sys
from urllib import request
from urllib.parse import urlencode



if __name__ == "__main__":
    post_dicts = {"email": sys.argv[2]}
    url_encoded_data = urlencode(post_dicts)
    post_data = url_encoded_data.encode("utf-8")
    req = request.Request(sys.argv[1], post_data)
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
