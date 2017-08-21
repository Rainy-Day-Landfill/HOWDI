#!/usr/bin/python3
# Phanes 2017-08-21

from lxml import html
import requests

# Synopsis
# Retrieves 99 proxies from sslproxies.org

def Main():

    proxy_source_url = "https://www.sslproxies.org"

    page = requests.get(proxy_source_url)

    tree = html.fromstring( page.content )

    ips = tree.xpath('//*[@id="proxylisttable"]/tbody/tr/td[1]')
    ports = tree.xpath('//*[@id="proxylisttable"]/tbody/tr/td[2]')

    for idx, val in enumerate(ips):
        print("{}:{}".format(ips[idx].text, ports[idx].text))

if __name__ == "__main__":
    Main()