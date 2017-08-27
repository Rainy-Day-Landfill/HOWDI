#!/usr/bin/python3
from proxy_sources.proxy_sources import ScraperPlexor
from proxy_checker.proxy_checker import ProxyChecker
from proxy_server.proxy_server import ProxyServer


def Main():
    proxy_list = list()
    filtered_proxy_list = list()
    local_proxy = "127.0.0.1:1999"

    # We're makin' a list...
    for proxy in ScraperPlexor.get_proxies():
        #print( proxy )
        proxy_list.append(proxy)

    # And we're checkin' it twice...
    proxy_list = list( set(proxy_list) )

    print("[II] [main] {} total proxies after filtering..".format(len(proxy_list)))

    # Gonna find out who's naughty or nice...
    for proxy in ProxyChecker.check_proxies(proxy_list, 8):
        # async checks of each result so that the final list only has
        # confirmed proxies.  if request takes longer than 1 second it will
        # not be added to the list.

        filtered_proxy_list.append(proxy)
        print("[II] [main] VERIFIED PROXY: {}".format(proxy))

    print("[II] [main] {} proxies passed health check".format(len(filtered_proxy_list)))
    print("[II] [main] You may now point your browser to {} and browse the net.".format(local_proxy))
    print("[II] [main] Proxies will be cycled automatically as errors occur.")

    # Dynamic L4 Proxies are comin' to town...
    for proxy in filtered_proxy_list:
        server = ProxyServer(proxy, local_proxy)
        print("[II] [main] OPEN TEE [{}] -> [{}]".format(local_proxy, proxy))
        server.main_loop()

if __name__=='__main__':
    Main()