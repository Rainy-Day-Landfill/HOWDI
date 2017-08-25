#!/usr/bin/python3

from proxy_sources.proxy_sources import ScraperPlexor

for proxy in ScraperPlexor.get_proxies():
    print( proxy  )
