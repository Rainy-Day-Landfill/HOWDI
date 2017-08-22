#!/usr/bin/python3
# Phanes 2017

from lxml import html
import requests

# Synopsis
# Retrieves up to 64 US proxies from hidemy.name

def Main():

    proxy_source_url = "https://hidemy.name/en/proxy-list/?country=US&maxtime=1000&type=hs#list"
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"

    headers = {
        'User-Agent': user_agent,
        'Reason': 'Stop charging for API access you assholes.'
    }

    page = requests.get(proxy_source_url, headers=headers)
    tree = html.fromstring( page.content )

    ips = tree.xpath('//*[@id="content-section"]/section[1]/div/table/tbody/tr/td[1]')
    ports = tree.xpath('//*[@id="content-section"]/section[1]/div/table/tbody/tr/td[2]')

    for idx, val in enumerate(ips):
            print("{}:{}".format(ips[idx].text, ports[idx].text))

if __name__ == "__main__":
    Main()
