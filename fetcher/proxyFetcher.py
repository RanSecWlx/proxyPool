# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     proxyFetcher
   Description :
   Author :        007x
   date：          2016/11/25
-------------------------------------------------
   Change Activity:
                   2016/11/25: proxyFetcher
-------------------------------------------------
"""
__author__ = '007x'

import os
import re
import json
import fileinput
from time import sleep
from lxml import html
from util.webRequest import WebRequest
from lxml.etree import tostring
from handler.configHandler import ConfigHandler

class ProxyFetcher(object):
    """
    proxy getter
    """
    
    conf = ConfigHandler()
    proxyInfor = conf.apiProxyConfig
    if len(proxyInfor) >= 8:
        proxiesInfor = {"http": proxyInfor, "https": proxyInfor}
    else:
        proxiesInfor = None

    @classmethod
    def freeProxy01(cls):
        """
        站大爷 https://www.zdaye.com/dayProxy.html
        """
        start_url = "https://www.zdaye.com/dayProxy.html"
        html_tree = WebRequest().get(start_url, verify=False).tree
        latest_page_time = html_tree.xpath("//span[@class='thread_time_info']/text()")[0].strip()
        from datetime import datetime
        interval = datetime.now() - datetime.strptime(latest_page_time, "%Y/%m/%d %H:%M:%S")
        if interval.seconds < 300:  # 只采集5分钟内的更新
            target_url = "https://www.zdaye.com/" + html_tree.xpath("//h3[@class='thread_title']/a/@href")[0].strip()
            while target_url:
                _tree = WebRequest().get(target_url, verify=False).tree
                for tr in _tree.xpath("//table//tr"):
                    ip = "".join(tr.xpath("./td[1]/text()")).strip()
                    port = "".join(tr.xpath("./td[2]/text()")).strip()
                    yield "%s:%s" % (ip, port)
                next_page = _tree.xpath("//div[@class='page']/a[@title='下一页']/@href")
                target_url = "https://www.zdaye.com/" + next_page[0].strip() if next_page else False
                sleep(5)

    @classmethod
    def freeProxy02(cls):
        """
        代理66 http://www.66ip.cn/
        """
        url = "http://www.66ip.cn/"
        resp = WebRequest().get(url, timeout=10).tree
        for i, tr in enumerate(resp.xpath("(//table)[3]//tr")):
            if i > 0:
                ip = "".join(tr.xpath("./td[1]/text()")).strip()
                port = "".join(tr.xpath("./td[2]/text()")).strip()
                yield "%s:%s" % (ip, port)

    @classmethod
    def freeProxy03(cls):
        """ 开心代理 """
        target_urls = ["http://www.kxdaili.com/dailiip.html", "http://www.kxdaili.com/dailiip/2/1.html"]
        for url in target_urls:
            tree = WebRequest().get(url).tree
            for tr in tree.xpath("//table[@class='active']//tr")[1:]:
                ip = "".join(tr.xpath('./td[1]/text()')).strip()
                port = "".join(tr.xpath('./td[2]/text()')).strip()
                yield "%s:%s" % (ip, port)

    @classmethod
    def freeProxy04(cls):
        """ FreeProxyList https://www.freeproxylists.net/zh/ """
        url = "https://www.freeproxylists.net/zh/?c=CN&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=50"
        tree = WebRequest().get(url, verify=False).tree
        from urllib import parse

        def parse_ip(input_str):
            html_str = parse.unquote(input_str)
            ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', html_str)
            return ips[0] if ips else None

        for tr in tree.xpath("//tr[@class='Odd']") + tree.xpath("//tr[@class='Even']"):
            ip = parse_ip("".join(tr.xpath('./td[1]/script/text()')).strip())
            port = "".join(tr.xpath('./td[2]/text()')).strip()
            if ip:
                yield "%s:%s" % (ip, port)

    @classmethod
    def freeProxy05(cls, page_count=1):
        """ 快代理 https://www.kuaidaili.com """
        url_pattern = [
            'https://www.kuaidaili.com/free/inha/{}/',
            'https://www.kuaidaili.com/free/intr/{}/'
        ]
        url_list = []
        for page_index in range(1, page_count + 1):
            for pattern in url_pattern:
                url_list.append(pattern.format(page_index))

        for url in url_list:
            tree = WebRequest().get(url).tree
            proxy_list = tree.xpath('.//table//tr')
            sleep(1)  # 必须sleep 不然第二条请求不到数据
            for tr in proxy_list[1:]:
                yield ':'.join(tr.xpath('./td/text()')[0:2])

    @classmethod
    def freeProxy06(cls):
        """ 冰凌代理 https://www.binglx.cn """
        url = "https://www.binglx.cn/?page=1"
        try:
            tree = WebRequest().get(url).tree
            proxy_list = tree.xpath('.//table//tr')
            for tr in proxy_list[1:]:
                yield ':'.join(tr.xpath('./td/text()')[0:2])
        except Exception as e:
            print(e)

    @classmethod
    def freeProxy07(cls):
        """ 云代理 """
        urls = ['http://www.ip3366.net/free/?stype=1', "http://www.ip3366.net/free/?stype=2"]
        for url in urls:
            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
            for proxy in proxies:
                yield ":".join(proxy)

    @classmethod
    def freeProxy08(cls):
        """ 小幻代理 """
        urls = ['https://ip.ihuan.me/address/5Lit5Zu9.html']
        for url in urls:
            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(r'>\s*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*?</a></td><td>(\d+)</td>', r.text)
            for proxy in proxies:
                yield ":".join(proxy)

    @classmethod
    def freeProxy09(cls, page_count=1):
        """ 免费代理库 """
        for i in range(1, page_count + 1):
            url = 'http://ip.jiangxianli.com/?country=中国&page={}'.format(i)
            html_tree = WebRequest().get(url, verify=False).tree
            for index, tr in enumerate(html_tree.xpath("//table//tr")):
                if index == 0:
                    continue
                yield ":".join(tr.xpath("./td/text()")[0:2]).strip()

    @classmethod
    def freeProxy10(cls):
        """ 89免费代理 """
        r = WebRequest().get("https://www.89ip.cn/index_1.html", timeout=10)
        proxies = re.findall(
            r'<td.*?>[\s\S]*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})[\s\S]*?</td>[\s\S]*?<td.*?>[\s\S]*?(\d+)[\s\S]*?</td>',
            r.text)
        for proxy in proxies:
            yield ':'.join(proxy)

    @classmethod
    def freeProxy11(cls):
        """ 稻壳代理 https://www.docip.net/ """
        r = WebRequest().get("https://www.docip.net/data/free.json", timeout=10)
        try:
            for each in r.json['data']:
                yield each['ip'], "HTTP"
        except Exception as e:
            print(e)

    @classmethod
    def freeProxy12(cls):
        """ 稻壳代理 https://proxylist.geonode.com/api/proxy-list """
        target_urls=[
            'https://proxylist.geonode.com/api/proxy-list?protocols=http&limit=500&page=1&sort_by=lastChecked&sort_type=desc',
            'https://proxylist.geonode.com/api/proxy-list?protocols=socks4&limit=500&page=1&sort_by=lastChecked&sort_type=desc',
            'https://proxylist.geonode.com/api/proxy-list?protocols=socks5&limit=500&page=1&sort_by=lastChecked&sort_type=desc'
        ]

        for url in target_urls:
            try:
                #r = WebRequest().get(url, proxies, verify=False, timeout=10)
                r = WebRequest().get(url, verify=False, timeout=10)
                for each in r.json['data']:
                    yield "%s:%s" % ( each['ip'], each['port'] ), each["protocols"][0]
            except Exception as e:
                print(e)
                pass

    @classmethod
    def freeProxy13(cls):
        """ 稻壳代理 https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/ """
        
        target_urls = [
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt'
        ]
        proxy_types = [
            "HTTP",    
            "HTTPS",
            "SOCKS4",
            "SOCKS5"
        ]

        for url in target_urls:
            try:
                if url.endswith("http.txt"):
                    proxy_type = proxy_types[0]
                elif url.endswith("https.txt"):
                    proxy_type = proxy_types[1]
                elif url.endswith("socks4.txt"):
                    proxy_type = proxy_types[2]
                elif url.endswith("socks5.txt"):
                    proxy_type = proxy_types[3]

                r = WebRequest().get(url, proxies = cls.proxiesInfor, verify=False, timeout=10)
                for each in r.text.splitlines():
                    yield each, proxy_type
            except Exception as e:
                print(e)
                pass

    @classmethod
    def freeProxy96(cls):
        target_urls = [
            'https://106.14.14.210/proxies_status',
            'http://47.243.63.109:5000/proxies_status',
            'http://142.171.31.40:5010/proxies_status',
        ]
        proxy_types = [
            "HTTP",
            "HTTPS",
            "SOCKS4",
            "SOCKS5"
        ]

        for url in target_urls:
            try:
                #r = WebRequest().get(url, verify=False, timeout=10)
                import requests
                r = requests.get(url, verify=False, timeout=10)
                #print(json.dumps(r.text))
                if r.status_code == 200:
                    for item in r.json()['proxies']:
                        each = f"{item['ip']}:{item['port']}"
                        proxy_type = item['protocol']
                        yield each, proxy_type
                else:
                    print(url, len(r.text))

            except Exception as e:
                print(e)
                pass


    @classmethod
    def freeProxy97(cls):
        """ http://example.com/en/ """
        # URL
        url = 'https://geoxy.io/proxies?page=%d&count=50'
	
	# 请求头
        headers = {
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'BgPXfhUc8CAhK7wGOqzqz9m77j3sH7',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://geoxy.io/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36',
        }
	
        pageid = 1
        target_url = url % pageid
        while True:
            try:
                r = WebRequest().get(target_url, header=headers, verify=False, timeout = 10)
                for each in r.json:
                    proxy_str = each['address']
                    proxy_type = "/".join(each['protocols'])
                    #print(proxy_str, proxy_type)
                    yield proxy_str, proxy_type
                if pageid >= 16:
                    break
                pageid += 1
                target_url = url % pageid

            except Exception as e:
                print(e)
                break
            

    @classmethod
    def freeProxy98(cls):
        """ http://example.com/en/ """
        target_urls=[
            "http://42.192.20.108:5000/all/",
            "http://117.72.44.211:5010/all/",
            "http://124.221.144.122:5010/all/",
            "http://119.45.214.228:5010/all/",
            "http://106.52.214.84:5010/all/",
            "http://152.69.217.58:5010/all/",
            "http://47.116.207.92:5010/all/"
        ]

        for url in target_urls:
            try:
                r = WebRequest().get(url, verify=False, timeout=10)
                for each in r.json:
                    #print(each['proxy'], "HTTP")
                    yield each['proxy'], "HTTP"
            except Exception as e:
                print(e)
                pass

    @classmethod
    def freeProxy99(cls):
        """ http://example.com/en/ """
	
	# URL
        url = 'https://proxyelite.info/free-proxy-list/?utm_referrer=https%3A%2F%2Fproxyelite.info%2F'
	
	# 请求头
        headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'no-cache',
	    'cookie': 'bhnTfg=wFEMWaiPAUCrQezVRxkpgHfnoIZKmj; _ga=GA1.1.333839908.1730476180; _gcl_au=1.1.2036505239.1730476192; _ym_uid=1730476195347327949; _ym_d=1730476195; wordpress_test_cookie=WP%20Cookie%20check; _ym_isad=1; _ym_visorc=w; _ga_S5PS0TSJE6=GS1.1.1730552817.3.1.1730553129.0.0.0; bhnTfg_hits=48; wFEMWaiPAUCrQezVRxkpgHfnoIZKmj=b2960ca1472f8689fc92c3b448ea3dfc-1730553131-1730553128',
	    'pragma': 'no-cache',
	    'priority': 'u=0, i',
	    'referer': 'https://proxyelite.info/free-proxy-list/',
	    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
	    'sec-ch-ua-arch': '""',
	    'sec-ch-ua-bitness': '"64"',
	    'sec-ch-ua-full-version': '"130.0.6723.70"',
	    'sec-ch-ua-full-version-list': '"Chromium";v="130.0.6723.70", "Google Chrome";v="130.0.6723.70", "Not?A_Brand";v="99.0.0.0"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-model': '"Nexus 5"',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-ch-ua-platform-version': '"6.0"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36',
        }
	
	# 请求数据
        data = {
	    'action': 'proxylister_load_more',
	    'nonce': '3d3e163d5f',
	    'page': '1',
	    'atts[downloads]': 'true'
	}
	
        over = 0
        pageid = 1
        while True:
            # 发送 POST 请求
            try:
                r = WebRequest().post(url, header=headers, data=data, verify=False, timeout = 10)

	        # 打印响应内容
                #print(r.text)
                #print(r.json['data']['rows'])
                #_tree = html.fromstring(r.json['data']['rows'])
                _tree = html.fromstring(r.text) 
                #print(tostring(_tree, pretty_print=True, encoding='unicode'))
                for tr in _tree.xpath("//table//tr"):
                    ip = "".join(tr.xpath("./td[1]/text()")).strip()
                    port = "".join(tr.xpath("./td[2]/text()")).strip()
                    proxy_type = "".join(tr.xpath("./td[3]/text()")).strip()
                    etstr = "".join(tr.xpath("./td[10]/text()")).strip().split()
                    #print(len(etstr), "".join(tr.xpath("./td[10]/text()")).strip())
                    if len(etstr) >= 2 and "分钟" not in etstr[1]:
                        over = 1
                        break
                    #print(ip, port, proxy_type)
                    yield "%s:%s" % (ip, port), proxy_type
                if over == 0:
                    if pageid > 10:
                        break
                    pageid += 1
                    data['page'] = '%d' % pageid
                else:
                    break
            except Exception as e:
                print(e)
                break
            
    @classmethod
    def freeProxy100(cls):
        """ http://example.com/en/ """

        over = 0
        pageid = 1
        target_url='https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=%d' % pageid
        while target_url:
            #print(target_url)
            r = WebRequest().get(target_url, verify=False, timeout=10)
            _tree = html.fromstring(r.text)
            #print(tostring(_tree, pretty_print=True, encoding='unicode'))
            for tr in _tree.xpath("//table//tr"):
                #print(tostring(tr, pretty_print=True, encoding='unicode')[:64])
                ip = "".join(tr.xpath("./td[1]/text()")).strip()
                if ip == "":
                    continue
                port = "".join(tr.xpath("./td[2]/a/text()")).strip()
                if port == "":
                    continue
                proxy_type = "".join(tr.xpath("./td[6]/a/text()")).strip()
                if proxy_type == "":
                    continue
                etstr = "".join(tr.xpath("./td[8]/text()")).strip().split()
                if len(etstr) >= 2 and "minutes" not in etstr[1]:
                    over = 1
                    break
                #print(ip, port, proxy_type)
                yield "%s:%s" % (ip, port), proxy_type    
            if over == 0:
                if pageid > 10:
                    break
                pageid += 1
                target_url = 'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=%d' % pageid
            else:
                break


    @classmethod
    def freeProxy101(cls):
        """ read proxy lists from file """

        filelist = [
            './proxyList/http.txt',        
            './proxyList/https.txt',        
            './proxyList/socks4.txt',        
            './proxyList/socks5.txt',        
        ]

        proxy_types = [
            "HTTP",    
            "HTTPS",
            "SOCKS4",
            "SOCKS5"
        ]

        try:
            for fl in filelist:
                if not os.path.exists(fl):
                    continue
                if os.path.getsize(fl) < 8:
                    continue
                if fl.endswith("http.txt"):
                    proxy_type = proxy_types[0]
                elif fl.endswith("https.txt"):
                    proxy_type = proxy_types[1]
                elif fl.endswith("socks4.txt"):
                    proxy_type = proxy_types[2]
                elif fl.endswith("socks5.txt"):
                    proxy_type = proxy_types[3]

                for line in fileinput.input(fl):
                    proxy = line.strip()
                    proxy = proxy.upper().replace(f"{proxy_type}://", "")
                    yield proxy, proxy_type 
                

        except Exception as e:
            print(e)
            pass



        """
        latest_page_time = html_tree.xpath("//span[@class='thread_time_info']/text()")[0].strip()
        from datetime import datetime
        interval = datetime.now() - datetime.strptime(latest_page_time, "%Y/%m/%d %H:%M:%S")
        if interval.seconds < 300:  # 只采集5分钟内的更新
            target_url = "https://www.zdaye.com/" + html_tree.xpath("//h3[@class='thread_title']/a/@href")[0].strip()
            while target_url:
                _tree = WebRequest().get(target_url, verify=False).tree
                for tr in _tree.xpath("//table//tr"):
                    ip = "".join(tr.xpath("./td[1]/text()")).strip()
                    port = "".join(tr.xpath("./td[2]/text()")).strip()
                    yield "%s:%s" % (ip, port)
                next_page = _tree.xpath("//div[@class='page']/a[@title='下一页']/@href")
                target_url = "https://www.zdaye.com/" + next_page[0].strip() if next_page else False
                sleep(5)

        
        try:
            for each in r.text.splitlines():
                yield each, "http"
        except Exception as e:
            print(e)
        """
    # @classmethod
    # def wallProxy01(cls):
    #     """
    #     PzzQz https://pzzqz.com/
    #     """
    #     from requests import Session
    #     from lxml import etree
    #     session = Session()
    #     try:
    #         index_resp = session.get("https://pzzqz.com/", timeout=20, verify=False).text
    #         x_csrf_token = re.findall('X-CSRFToken": "(.*?)"', index_resp)
    #         if x_csrf_token:
    #             data = {"http": "on", "ping": "3000", "country": "cn", "ports": ""}
    #             proxy_resp = session.post("https://pzzqz.com/", verify=False,
    #                                       headers={"X-CSRFToken": x_csrf_token[0]}, json=data).json()
    #             tree = etree.HTML(proxy_resp["proxy_html"])
    #             for tr in tree.xpath("//tr"):
    #                 ip = "".join(tr.xpath("./td[1]/text()"))
    #                 port = "".join(tr.xpath("./td[2]/text()"))
    #                 yield "%s:%s" % (ip, port)
    #     except Exception as e:
    #         print(e)

    # @classmethod
    # def freeProxy10(cls):
    #     """
    #     墙外网站 cn-proxy
    #     :return:
    #     """
    #     urls = ['http://cn-proxy.com/', 'http://cn-proxy.com/archives/218']
    #     request = WebRequest()
    #     for url in urls:
    #         r = request.get(url, timeout=10)
    #         proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\w\W]<td>(\d+)</td>', r.text)
    #         for proxy in proxies:
    #             yield ':'.join(proxy)

    # @classmethod
    # def freeProxy11(cls):
    #     """
    #     https://proxy-list.org/english/index.php
    #     :return:
    #     """
    #     urls = ['https://proxy-list.org/english/index.php?p=%s' % n for n in range(1, 10)]
    #     request = WebRequest()
    #     import base64
    #     for url in urls:
    #         r = request.get(url, timeout=10)
    #         proxies = re.findall(r"Proxy\('(.*?)'\)", r.text)
    #         for proxy in proxies:
    #             yield base64.b64decode(proxy).decode()

    # @classmethod
    # def freeProxy12(cls):
    #     urls = ['https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1']
    #     request = WebRequest()
    #     for url in urls:
    #         r = request.get(url, timeout=10)
    #         proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
    #         for proxy in proxies:
    #             yield ':'.join(proxy)


if __name__ == '__main__':
    p = ProxyFetcher()
    for each in p.freeProxy96():
        print(each)

# http://nntime.com/proxy-list-01.htm
