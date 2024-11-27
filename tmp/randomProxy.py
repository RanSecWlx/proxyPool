import sys
import os 
import json 
import random
import requests
import fileinput
import ipaddress
import subprocess
from urllib3.exceptions import InsecureRequestWarning

class randomProxy(object):
    def __init__(self, fpath):
        self._proxiesList = []
        self._outDir = "../proxyList/"
        self._readFile = fpath
        self.read_proxy_info()
        self._test_url_list = [
                'https://ifconfig.me/ip',
                #'https://ipinfo.io/ip',
                #'https://icanhazip.com',
                #'https://checkip.amazonaws.com',
                #'https://ipecho.net/plain',
                #'https://www.trackip.net/ip'
        ]
        self._test_count = 3
        self._request_timeout = 5

    def read_proxy_info(self):
        if not os.path.exists(self._readFile):
            return 
        if os.path.getsize(self._readFile) < 8:
            return 
        
        self._proxy_type = None
        if self._readFile.endswith("http.txt"):
            self._proxy_type = "http"
        elif self._readFile.endswith("https.txt"):
            self._proxy_type = "https"
        elif self._readFile.endswith("socks4.txt"):
            self._proxy_type = "socks4"
        elif self._readFile.endswith("socks5.txt"):
            self._proxy_type = "socks5"
        else:
            self._proxy_type = None

        for line in fileinput.input(self._readFile):
            if len(line) < 9:
                continue
            if self._proxy_type is None:
                proxy = line.strip()
            else:
                proxy = f"{self._proxy_type}://{line.strip()}"

            self._proxiesList.append(proxy)

    def get_random_proxy(self):
        if len(self._proxiesList) == 0:
            return None
        return random.choice(self._proxiesList)

    def is_network_reachable(self, proxy):

        id = 0
        proxies = {"http": proxy, "https": proxy}
        self._test_url = random.choice(self._test_url_list)
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        
        while id < self._test_count:
            try:
                id += 1
                #start_time = time.time()
                r = requests.get(self._test_url, proxies = proxies, verify=False, timeout=self._request_timeout)
                #end_time = time.time()
                #vist_time = end_time - start_time
                status_code = r.status_code
                #print(status_code, r.text)
                if status_code == 200:
                    try:
                        #print(status_code, r.text)
                        ip = ipaddress.ip_address(r.text)
                        #print(ip)
                        #print(proxy, r.status_code, id)
                        return ("%s ok") % proxy
                    except Exception as e:
                        #print(proxy, r.status_code, id)
                        #print(e)
                        pass
            except Exception as e:
                #print(proxy, "failed", id)
                #print(proxy, "failed")
                #print(e)
                pass
        
        return ("%s failed") % proxy

if __name__ == "__main__":
    randomProxyData = randomProxy("./proxies.conf")
    print(randomProxyData.is_network_reachable(sys.argv[1]))
