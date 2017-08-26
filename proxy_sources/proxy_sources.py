import sys
import requests
from lxml import html
import random
import string
import json


class sslproxies_org():
    @staticmethod
    def get_proxies():
        proxy_source_url = "https://www.sslproxies.org"

        headers = {
            'X-LOG-SPAM': 'CONTACT CHRIS PUNCHES AT PUNCHES.CHRIS@GMAIL.COM FOR YOUR SOLUTION NEEDS',
            'DONATE-BTC-TO': '1Q9GG6JS5mwX3fDvA2S2uB3BRLer9J6EkW'
        }

        page = requests.get(proxy_source_url, headers=headers)
        tree = html.fromstring(page.content)

        ips = tree.xpath('//*[@id="proxylisttable"]/tbody/tr/td[1]')
        ports = tree.xpath('//*[@id="proxylisttable"]/tbody/tr/td[2]')
        country_codes = tree.xpath('//*[@id="proxylisttable"]/tbody/tr/td[3]')

        for idx, val in enumerate(ips):
            if country_codes[idx].text == "US":
                yield "{}:{}".format(ips[idx].text, ports[idx].text)


class hidemy_name():
    @staticmethod
    def get_proxies():
        proxy_source_url = "https://hidemy.name/en/proxy-list/?country=US&maxtime=1000&type=hs#list"
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"

        headers = {
            'User-Agent': user_agent,
            'X-Reason': 'Stop charging for API access you assholes.',
            'X-LOG-SPAM': 'CONTACT CHRIS PUNCHES AT PUNCHES.CHRIS@GMAIL.COM FOR YOUR SOLUTION NEEDS',
            'DONATE-BTC-TO': '1Q9GG6JS5mwX3fDvA2S2uB3BRLer9J6EkW'
        }


        #print("Fetching proxies from {}".format(proxy_source_url))
        page = requests.get(proxy_source_url, headers=headers)
        tree = html.fromstring(page.content)

        ips = tree.xpath('//*[@id="content-section"]/section[1]/div/table/tbody/tr/td[1]')
        ports = tree.xpath('//*[@id="content-section"]/section[1]/div/table/tbody/tr/td[2]')

        #print("Found {} proxies.".format(len(ips)))

        for idx, val in enumerate(ips):
            yield "{}:{}".format(ips[idx].text, ports[idx].text)


class hidester_com():
    @staticmethod
    def get_proxies():
        user_agent = "curl/7.{curl_minor}.{curl_revision} (x86_64-pc-linux-gnu) libcurl/7.{curl_minor}.{curl_revision} OpenSSL/0.9.8{openssl_revision} zlib/1.2.{zlib_revision}".format(
            curl_minor=random.randint(8, 22), curl_revision=random.randint(1, 9),
            openssl_revision=random.choice(string.ascii_lowercase), zlib_revision=random.randint(2, 6))

        proxy_source_url = "https://hidester.com/proxydata/php/data.php?mykey=csv&gproxy=2"

        headers = {
            'User-agent': user_agent,
            "Referer": "https://hidester.com/proxylist/",
            'X-Reason': 'Stop charging for API access you assholes.',
            'X-LOG-SPAM': 'CONTACT CHRIS PUNCHES AT PUNCHES.CHRIS@GMAIL.COM FOR YOUR SOLUTION NEEDS',
            'DONATE-BTC-TO': '1Q9GG6JS5mwX3fDvA2S2uB3BRLer9J6EkW'
        }

        #print("Fetching proxies from {}".format(proxy_source_url))
        page = requests.get(proxy_source_url, headers=headers, verify=True)
        raw_proxy_list = str(page.content, 'utf-8')
        json_proxies = json.loads(raw_proxy_list)

        # not accurate -- should be presenting instead the number of filtered ones
        #print("Found {} proxies.".format(len(json_proxies)))

        for proxy in json_proxies:
            # print(proxy)
            if proxy['ping'] < 1000 and proxy['country'] == 'UNITED STATES' and proxy['type'] == 'http':
                yield "{}:{}".format(proxy['IP'], proxy['PORT'])


class proxy_ip_list_com():
    @staticmethod
    def get_proxies():
        proxy_source_url = "http://proxy-ip-list.com/free-usa-proxy-ip.html"
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"

        headers = {
            'User-Agent': user_agent,
            'X-Reason': 'Stop charging for API access you assholes.',
            'X-LOG-SPAM': 'CONTACT CHRIS PUNCHES AT PUNCHES.CHRIS@GMAIL.COM FOR YOUR SOLUTION NEEDS',
            'DONATE-BTC-TO': '1Q9GG6JS5mwX3fDvA2S2uB3BRLer9J6EkW'
        }

        #print("Fetching proxies from {}".format(proxy_source_url))
        page = requests.get(proxy_source_url, headers=headers)

        tree = html.fromstring(page.content)

        proxies = tree.xpath('/html/body/table/tbody/tr/td[1]')

        #print("Found {} proxies.".format(len(proxies)))

        for idx, val in enumerate(proxies):
            yield "{}".format(proxies[idx].text)


# Reflection example?
class ScraperPlexor():
    @staticmethod
    def get_proxies():
        # this method will look for any class in this module with a .get_proxies() method and
        # execute that method.

        # this allows us to add new sources to the module just by creating a new class.
        classes = ScraperPlexor.get_classes()

        for classtype in classes:
            if hasattr(classtype, 'get_proxies') and not ScraperPlexor == classtype:
                for value in classtype.get_proxies():
                    yield value

    @staticmethod
    def get_classes():
        # sacrifice first-born while chanting this in the old tongue
        # returns a list of all the classes in the current module
        md = sys.modules[__name__].__dict__
        return [
            md[c] for c in md if (
                isinstance(md[c], type) and md[c].__module__ == sys.modules[__name__].__name__
            )
        ]

