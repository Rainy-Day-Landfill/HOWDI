#!/usr/bin/python3
# Phanes 2017

from lxml import html
import requests

# Synopsis
# Retrieves up to 99 US proxies from sslproxies.org

def Main():

    proxy_source_url = "https://www.sslproxies.org"

    page = requests.get(proxy_source_url)

    tree = html.fromstring( page.content )

    ips = tree.xpath('//*[@id="proxylisttable"]/tbody/tr/td[1]')
    ports = tree.xpath('//*[@id="proxylisttable"]/tbody/tr/td[2]')
    country_codes = tree.xpath('//*[@id="proxylisttable"]/tbody/tr/td[3]')


    for idx, val in enumerate(ips):
        if country_codes[idx].text == "US":
            print("{}:{}".format(ips[idx].text, ports[idx].text))

if __name__ == "__main__":
    Main()
