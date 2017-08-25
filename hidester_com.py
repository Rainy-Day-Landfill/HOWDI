#!/usr/bin/python3
# Phanes 2017

from lxml import html
import requests
import random
import string
import json

# Synopsis
# Retrieves up to all freely listed US proxies from hidester.com

def Main():
    user_agent = "curl/7.{curl_minor}.{curl_revision} (x86_64-pc-linux-gnu) libcurl/7.{curl_minor}.{curl_revision} OpenSSL/0.9.8{openssl_revision} zlib/1.2.{zlib_revision}".format(
        curl_minor=random.randint(8, 22), curl_revision=random.randint(1, 9),
        openssl_revision=random.choice(string.ascii_lowercase), zlib_revision=random.randint(2, 6))

    proxy_source_url = "https://hidester.com/proxydata/php/data.php?mykey=csv&gproxy=2"

    headers = {
        'User-agent': user_agent,
        "Referer": "https://hidester.com/proxylist/",
        'Reason': 'Stop charging for API access you assholes.'
    }

    page = requests.get(proxy_source_url, headers=headers, verify=True)
    raw_proxy_list = str( page.content, 'utf-8')
    json_proxies = json.loads( raw_proxy_list )
    for proxy in json_proxies:
        # print(proxy)
        if proxy['ping'] < 1000 and proxy['country'] == 'UNITED STATES' and proxy['type'] == 'http':
            print("{}:{}".format(proxy['IP'], proxy['PORT']))

if __name__ == "__main__":
    Main()
