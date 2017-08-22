#!/usr/bin/python3
# Phanes 2017

from lxml import html
import requests

# Synopsis
# Retrieves up to all freely listed US proxies from proxy-ip-list.com

def Main():

    proxy_source_url = "http://proxy-ip-list.com/free-usa-proxy-ip.html"
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"

    headers = {
        'User-Agent': user_agent,
        'Reason': 'Stop charging for API access you assholes.'
    }

    page = requests.get(proxy_source_url, headers=headers)
    tree = html.fromstring( page.content )

    proxies = tree.xpath('/html/body/table/tbody/tr/td[1]')

    for idx, val in enumerate(proxies):
            print("{}".format(proxies[idx].text))

if __name__ == "__main__":
    Main()
