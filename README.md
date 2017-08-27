# HTTP Operations With Dynamic Input.
This is a browser IP anonymizer that pulls its proxies from various lists, then sets up an L4 bound to a local port to relay to the upstream proxies that it finds.  Use responsibly.

# Usage
It's literally so easy to use that if you can't figure out how to use it than you shouldn't be using it.

---
## Sample output:
~~~~
[ phanes@prime.surroindustries.lan ] << ~/development/proxy-scraper >>

[- ./proxy-scraper.py
[II] [proxy-ip-list.com] Fetching proxy list.
[II] [proxy-ip-list.com] Found 26 proxies.
[II] [hidemy.name] Fetching proxy list.
[II] [hidemy.name] Found 50 proxies.
[II] [hidester.com] Fetching proxy list.
[II] [hidester.com] Found 1448 proxies.
[II] [www.sslproxies.org] Fetching proxy list.
[II] [www.sslproxies.org] Found 100 proxies.
[II] [awmproxy.net] Fetching proxy list.
[II] [awmproxy.net] Found 12746 proxies.
[II] [main] 2070 total proxies after filtering..
[II] [proxy_checker] Checking health of proxies
[II] [main] VERIFIED PROXY: 38.87.236.84:63909
[II] [main] VERIFIED PROXY: 47.88.12.112:3128
[II] [main] VERIFIED PROXY: 45.77.34.110:3128
[II] [main] VERIFIED PROXY: 45.77.26.47:3128
[II] [main] VERIFIED PROXY: 205.189.37.86:53281
[II] [main] VERIFIED PROXY: 162.243.171.75:8080
[II] [main] VERIFIED PROXY: 138.197.83.21:80
[II] [main] VERIFIED PROXY: 93.188.161.129:8080
[II] [main] VERIFIED PROXY: 45.76.55.34:8080
[II] [main] VERIFIED PROXY: 98.191.98.146:3128
[II] [main] VERIFIED PROXY: 159.63.166.167:53281
[II] [main] VERIFIED PROXY: 138.197.83.21:3128
[II] [main] VERIFIED PROXY: 104.131.118.88:3128
[II] [main] VERIFIED PROXY: 138.68.16.252:3128
[II] [main] VERIFIED PROXY: 45.77.26.47:8080
[II] [main] VERIFIED PROXY: 107.155.85.168:3128
[II] [main] VERIFIED PROXY: 104.236.13.100:8888
[II] [main] VERIFIED PROXY: 199.127.101.139:53281
[II] [main] VERIFIED PROXY: 184.185.166.27:8080
[II] [main] VERIFIED PROXY: 12.252.97.86:53281
[II] [main] VERIFIED PROXY: 104.236.110.244:8080
[II] [main] VERIFIED PROXY: 159.203.123.120:3128
[II] [main] VERIFIED PROXY: 67.205.160.136:3128
[II] [main] VERIFIED PROXY: 45.77.52.98:80
[II] [main] VERIFIED PROXY: 45.76.182.180:3128
[II] [main] VERIFIED PROXY: 199.195.253.124:3128
[II] [main] VERIFIED PROXY: 138.68.16.252:8888
[II] [main] VERIFIED PROXY: 207.251.53.67:53281
[II] [main] VERIFIED PROXY: 165.227.124.88:8080
[II] [main] VERIFIED PROXY: 45.76.93.19:8118
[II] [main] VERIFIED PROXY: 104.131.118.88:80
[II] [main] VERIFIED PROXY: 70.63.251.182:53281
[II] [main] VERIFIED PROXY: 47.52.5.8:3128
[II] [main] VERIFIED PROXY: 165.227.124.88:80
[II] [main] VERIFIED PROXY: 67.205.172.65:3128
[II] [main] VERIFIED PROXY: 184.105.43.114:63909
[II] [main] VERIFIED PROXY: 216.56.48.118:9000
[II] [main] VERIFIED PROXY: 192.241.150.54:8080
[II] [main] VERIFIED PROXY: 134.35.42.85:8080
[II] [main] VERIFIED PROXY: 199.195.251.143:3128
[II] [main] VERIFIED PROXY: 45.76.184.198:3128
[II] [main] VERIFIED PROXY: 139.60.178.121:53281
[II] [main] VERIFIED PROXY: 12.46.46.147:53281
[II] [main] VERIFIED PROXY: 146.148.123.229:3128
[II] [main] VERIFIED PROXY: 74.206.103.250:443
[II] [main] VERIFIED PROXY: 104.131.118.88:8080
[II] [main] VERIFIED PROXY: 64.185.120.62:53281
[II] [main] VERIFIED PROXY: 52.35.24.254:8080
[II] [main] VERIFIED PROXY: 108.161.135.81:3128
[II] [main] VERIFIED PROXY: 209.43.86.153:3128
[II] [main] VERIFIED PROXY: 198.35.55.147:443
[II] [main] VERIFIED PROXY: 34.196.219.241:3780
[II] [main] VERIFIED PROXY: 67.205.174.218:8080
[II] [main] VERIFIED PROXY: 98.150.238.48:63909
[II] [main] VERIFIED PROXY: 162.243.18.46:3128
[II] [main] VERIFIED PROXY: 138.197.83.21:8799
[II] [main] VERIFIED PROXY: 144.217.104.145:80
[II] [main] VERIFIED PROXY: 45.55.27.246:8080
[II] [main] VERIFIED PROXY: 104.236.110.244:80
[II] [main] VERIFIED PROXY: 45.77.52.98:3128
[II] [main] VERIFIED PROXY: 45.76.184.198:8080
[II] [main] VERIFIED PROXY: 138.68.16.252:80
[II] [main] VERIFIED PROXY: 162.223.88.243:80
[II] [main] VERIFIED PROXY: 66.85.19.190:65309
[II] [main] 64 proxies passed health check
[II] [main] You may now point your browser to 127.0.0.1:1999 and browse the net.
[II] [main] Proxies will be cycled automatically as errors occur.
[II] [main] OPEN TEE [127.0.0.1:1999] -> [38.87.236.84:63909]
[II] [proxy_server] [127.0.0.1:53656] connected
[II] [proxy_server] [127.0.0.1:53660] connected
[II] [proxy_server] [127.0.0.1:53662] connected
[II] [proxy_server] [127.0.0.1:53668] connected
[II] [proxy_server] [127.0.0.1:53672] connected
[WW] [proxy_server]  [127.0.0.1:53656] disconnected
[II] [main] OPEN TEE [127.0.0.1:1999] -> [47.88.12.112:3128]
[II] [proxy_server] [127.0.0.1:53678] connected
[II] [proxy_server] [127.0.0.1:53682] connected
[II] [proxy_server] [127.0.0.1:53684] connected
[II] [proxy_server] [127.0.0.1:53688] connected
[WW] [proxy_server]  [127.0.0.1:53684] disconnected
[II] [main] OPEN TEE [127.0.0.1:1999] -> [45.77.34.110:3128]
[II] [proxy_server] [127.0.0.1:53694] connected
[II] [proxy_server] [127.0.0.1:53698] connected
[II] [proxy_server] [127.0.0.1:53700] connected
[II] [proxy_server] [127.0.0.1:53704] connected
[II] [proxy_server] [127.0.0.1:53706] connected
[II] [proxy_server] [127.0.0.1:53708] connected
[II] [proxy_server] [127.0.0.1:53718] connected
[II] [proxy_server] [127.0.0.1:53722] connected
[II] [proxy_server] [127.0.0.1:53726] connected
[II] [proxy_server] [127.0.0.1:53730] connected
[II] [proxy_server] [127.0.0.1:53732] connected
[II] [proxy_server] [127.0.0.1:53734] connected
[II] [proxy_server] [127.0.0.1:53736] connected
[II] [proxy_server] [127.0.0.1:53738] connected
[II] [proxy_server] [127.0.0.1:53742] connected
[II] [proxy_server] [127.0.0.1:53754] connected
[WW] [proxy_server]  [127.0.0.1:53700] disconnected
[II] [main] OPEN TEE [127.0.0.1:1999] -> [45.77.26.47:3128]
[II] [proxy_server] [127.0.0.1:53758] connected
[II] [proxy_server] [127.0.0.1:53760] connected
[II] [proxy_server] [127.0.0.1:53764] connected
[WW] [proxy_server]  [127.0.0.1:53760] disconnected
[II] [main] OPEN TEE [127.0.0.1:1999] -> [205.189.37.86:53281]
[II] [proxy_server] [127.0.0.1:53770] connected
[II] [proxy_server] [127.0.0.1:53772] connected
[II] [proxy_server] [127.0.0.1:53780] connected
[II] [proxy_server] [127.0.0.1:53784] connected
[II] [proxy_server] [127.0.0.1:53786] connected
[II] [proxy_server] [127.0.0.1:53790] connected
[II] [proxy_server] [127.0.0.1:53792] connected
[II] [proxy_server] [127.0.0.1:53794] connected
[II] [proxy_server] [127.0.0.1:53796] connected
[II] [proxy_server] [127.0.0.1:53798] connected
[II] [proxy_server] [127.0.0.1:53804] connected
[II] [proxy_server] [127.0.0.1:53812] connected
[WW] [proxy_server]  [205.189.37.86:53281] disconnected
[II] [main] OPEN TEE [127.0.0.1:1999] -> [162.243.171.75:8080]
[II] [proxy_server] [127.0.0.1:53820] connected
[II] [proxy_server] [127.0.0.1:53822] connected
[II] [proxy_server] [127.0.0.1:53824] connected
[WW] [proxy_server]  [127.0.0.1:53824] disconnected
[II] [main] OPEN TEE [127.0.0.1:1999] -> [138.197.83.21:80]
[II] [proxy_server] [127.0.0.1:53832] connected
[II] [proxy_server] [127.0.0.1:53836] connected
[II] [proxy_server] [127.0.0.1:53840] connected
[II] [proxy_server] [127.0.0.1:53844] connected
[II] [proxy_server] [127.0.0.1:53846] connected
[II] [proxy_server] [127.0.0.1:53852] connected
[II] [proxy_server] [127.0.0.1:53854] connected
[II] [proxy_server] [127.0.0.1:53856] connected
[II] [proxy_server] [127.0.0.1:53864] connected
[II] [proxy_server] [127.0.0.1:53868] connected
[II] [proxy_server] [127.0.0.1:53872] connected
[II] [proxy_server] [127.0.0.1:53876] connected
[II] [proxy_server] [127.0.0.1:53880] connected
[II] [proxy_server] [127.0.0.1:53884] connected
[II] [proxy_server] [127.0.0.1:53886] connected
[II] [proxy_server] [127.0.0.1:53888] connected
[II] [proxy_server] [127.0.0.1:53890] connected
[II] [proxy_server] [127.0.0.1:53892] connected
[WW] [proxy_server]  [127.0.0.1:53886] disconnected
[II] [main] OPEN TEE [127.0.0.1:1999] -> [93.188.161.129:8080]
[II] [proxy_server] [127.0.0.1:53904] connected
[II] [proxy_server] [127.0.0.1:53908] connected
[II] [proxy_server] [127.0.0.1:53910] connected
[II] [proxy_server] [127.0.0.1:53912] connected
[WW] [proxy_server]  [127.0.0.1:53904] disconnected
[II] [main] OPEN TEE [127.0.0.1:1999] -> [45.76.55.34:8080]
[II] [proxy_server] [127.0.0.1:53920] connected
[II] [proxy_server] [127.0.0.1:53924] connected
[II] [proxy_server] [127.0.0.1:53928] connected
[II] [proxy_server] [127.0.0.1:53930] connected
[II] [proxy_server] [127.0.0.1:53934] connected
[II] [proxy_server] [127.0.0.1:53936] connected
[II] [proxy_server] [127.0.0.1:53944] connected
[II] [proxy_server] [127.0.0.1:53948] connected
[II] [proxy_server] [127.0.0.1:53952] connected
[WW] [proxy_server]  [127.0.0.1:53924] disconnected
[II] [main] OPEN TEE [127.0.0.1:1999] -> [98.191.98.146:3128]
[II] [proxy_server] [127.0.0.1:53956] connected
[II] [proxy_server] [127.0.0.1:53960] connected
[II] [proxy_server] [127.0.0.1:53962] connected
[II] [proxy_server] [127.0.0.1:53966] connected
[II] [proxy_server] [127.0.0.1:53968] connected
[II] [proxy_server] [127.0.0.1:53970] connected
[II] [proxy_server] [127.0.0.1:53980] connected
[II] [proxy_server] [127.0.0.1:53982] connected
[II] [proxy_server] [127.0.0.1:53986] connected
[II] [proxy_server] [127.0.0.1:53992] connected
[II] [proxy_server] [127.0.0.1:53996] connected
[II] [proxy_server] [127.0.0.1:54000] connected
[II] [proxy_server] [127.0.0.1:54004] connected
~~~~
