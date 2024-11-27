# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _validators
   Description :   定义proxy验证方法
   Author :        007x
   date：          2021/5/25
-------------------------------------------------
   Change Activity:
                   2023/03/10: 支持带用户认证的代理格式 username:password@ip:port
-------------------------------------------------
"""
__author__ = '007x'

import re
import time
import requests 
import ipaddress
from util.six import withMetaclass
from util.singleton import Singleton
from handler.configHandler import ConfigHandler

conf = ConfigHandler()

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
          'Accept': '*/*',
          'Connection': 'keep-alive',
          'Accept-Language': 'zh-CN,zh;q=0.8'}

IP_REGEX = re.compile(r"(.*:.*@)?\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}")


class ProxyValidator(withMetaclass(Singleton)):
    pre_validator = []
    http_validator = []
    https_validator = []

    @classmethod
    def addPreValidator(cls, func):
        cls.pre_validator.append(func)
        return func

    @classmethod
    def addHttpValidator(cls, func):
        cls.http_validator.append(func)
        return func

    @classmethod
    def addHttpsValidator(cls, func):
        cls.https_validator.append(func)
        return func


@ProxyValidator.addPreValidator
def formatValidator(proxy):
    """检查代理格式"""
    return True if IP_REGEX.fullmatch(proxy) else False


@ProxyValidator.addHttpValidator
def httpTimeOutValidator(oproxy):
    """ http检测超时 """
    proxy = oproxy.proxy
    if "HTTPS" in oproxy.proxy_type:
        proxies = {"http": "https://{proxy}".format(proxy=proxy), "https": "https://{proxy}".format(proxy=proxy)}
    elif "HTTP" in oproxy.proxy_type:
        proxies = {"http": "http://{proxy}".format(proxy=proxy), "https": "http://{proxy}".format(proxy=proxy)}
    elif "SOCKS4" in oproxy.proxy_type:
        proxies = {"http": "socks4://{proxy}".format(proxy=proxy), "https": "socks4://{proxy}".format(proxy=proxy)}
    elif "SOCKS5" in oproxy.proxy_type:
        proxies = {"http": "socks5://{proxy}".format(proxy=proxy), "https": "socks5://{proxy}".format(proxy=proxy)}
    else:
        proxies = {"http": "http://{proxy}".format(proxy=proxy), "https": "http://{proxy}".format(proxy=proxy)}
    
    start_time = time.perf_counter()
    try:
        #print(proxies, conf.httpUrl)
        r = requests.get(conf.httpUrl, headers=HEADER, proxies=proxies, timeout=conf.verifyTimeout)
        end_time = time.perf_counter()
        oproxy.resp_time = int((end_time - start_time) * 1000);
        #print(r.text)
        #if r.status_code != 200:
        #    print(r.status_code, conf.httpsUrl, proxies) 
        #print(oproxy.resp_time)
        """
        test proxy test by ifconfig.me
        """
        if r.status_code == 200:
            try:
                ip = ipaddress.ip_address(r.text)
                #print(ip)
                return True
            except Exception as e:
                #print(e)
                pass
        return False
        """ the original proxy test """
        #return True if r.status_code == 200 else False
    except Exception as e:
        #print(e)
        return False


@ProxyValidator.addHttpsValidator
def httpsTimeOutValidator(oproxy):
    """https检测超时"""
    proxy = oproxy.proxy
    if "HTTPS" in oproxy.proxy_type :
        proxies = {"http": "https://{proxy}".format(proxy=proxy), "https": "https://{proxy}".format(proxy=proxy)}
    elif "HTTP" in oproxy.proxy_type :
        proxies = {"http": "http://{proxy}".format(proxy=proxy), "https": "http://{proxy}".format(proxy=proxy)}
    elif "SOCKS4" in oproxy.proxy_type:
        proxies = {"http": "socks4://{proxy}".format(proxy=proxy), "https": "socks4://{proxy}".format(proxy=proxy)}
    elif "SOCKS5" in oproxy.proxy_type:
        proxies = {"http": "socks5://{proxy}".format(proxy=proxy), "https": "socks5://{proxy}".format(proxy=proxy)}
    else:
        proxies = {"http": "http://{proxy}".format(proxy=proxy), "https": "http://{proxy}".format(proxy=proxy)}
        
    start_time = time.perf_counter()
    try:
        #print(proxies, conf.httpsUrl)
        r = requests.get(conf.httpsUrl, headers=HEADER, proxies=proxies, timeout=conf.verifyTimeout, verify=False)
        end_time = time.perf_counter()
        oproxy.resp_time = int((end_time - start_time) * 1000);
        #print(r.text)
        #if r.status_code != 200:
        #    print(r.status_code, conf.httpsUrl, proxies)
        #print(oproxy.resp_time)
        """
        test proxy test by ifconfig.me
        """
        if r.status_code == 200:
            try:
                ip = ipaddress.ip_address(r.text)
                #print(ip)
                return True
            except Exception as e:
                #print(e)
                pass
        return False
        """ the original proxy test """
        #return True if r.status_code == 200 else False
    except Exception as e:
        #print(e)
        return False


@ProxyValidator.addHttpValidator
def customValidatorExample(proxy):
    """自定义validator函数，校验代理是否可用, 返回True/False"""
    return True
