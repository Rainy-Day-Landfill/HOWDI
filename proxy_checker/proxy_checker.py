import grequests
from urllib.parse import urlsplit
import random

class ProxyChecker():
    @staticmethod
    def check_proxies( proxy_list, threads=8 ):
        IFCONFIG_CANDIDATES = [
            "https://ifconfig.co/ip",
            "https://api.ipify.org/?format=text",
            "https://myexternalip.com/raw",
            "https://wtfismyip.com/text"
        ]
        # de-dupe
        proxy_list = list(set(proxy_list))

        # create a set of unsent requests
        rs = []
        for proxy in proxy_list:
            rs.append(  grequests.get( random.choice(IFCONFIG_CANDIDATES), proxies={ "http": proxy, "https": proxy}, timeout=1 ) )

        print("\nChecking proxies.  All valid proxies listed below:\n")

        working_proxies = []
        # send a few at a time in sets of size "threads"
        for response in grequests.imap(rs, size=threads):
            # raw_text = str( response.content, 'utf-8')
            if response.status_code == 200:
                this_proxy = next(iter(response.connection.proxy_manager))

                parsed = urlsplit( this_proxy ).netloc
                working_proxies.append( parsed )
                yield parsed