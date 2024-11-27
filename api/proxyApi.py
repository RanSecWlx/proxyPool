# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     ProxyApi.py
   Description :   WebApi
   Author :       007x
   date：          2016/12/4
-------------------------------------------------
   Change Activity:
                   2016/12/04: WebApi
                   2019/08/14: 集成Gunicorn启动方式
                   2020/06/23: 新增pop接口
                   2022/07/21: 更新count接口
-------------------------------------------------
"""
__author__ = '007x'
import re
import platform
from werkzeug.wrappers import Response
from flask import Flask, jsonify, request

from util.six import iteritems
from helper.proxy import Proxy
from handler.proxyHandler import ProxyHandler
from handler.configHandler import ConfigHandler
import json
from collections import OrderedDict

app = Flask(__name__)
conf = ConfigHandler()
proxy_handler = ProxyHandler()


class JsonResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (dict, list)):
            response = jsonify(response)

        return super(JsonResponse, cls).force_type(response, environ)


app.response_class = JsonResponse

api_list = [
    {"url": "/get", "params": "type: ''https'|''", "desc": "get a proxy"},
    {"url": "/pop", "params": "", "desc": "get and delete a proxy"},
    {"url": "/delete", "params": "proxy: 'e.g. 127.0.0.1:8080'", "desc": "delete an unable proxy"},
    {"url": "/all", "params": "type: ''https'|''", "desc": "get all proxy from proxy pool"},
    {"url": "/count", "params": "", "desc": "return proxy count"},
    {"url": "/clear", "params": "", "desc": "clear proxy"}
    # 'refresh': 'refresh proxy pool',
]


@app.after_request
def apply_caching(response):
    response.headers['Connection'] = 'close'
    return response

@app.route('/')
def index():
    return {'url': api_list}


@app.route('/get/')
def get():
    https = request.args.get("type", "").lower() == 'https'
    proxy = proxy_handler.get(https)
    return proxy.to_dict if proxy else {"code": 0, "src": "no proxy"}


@app.route('/pop/')
def pop():
    https = request.args.get("type", "").lower() == 'https'
    proxy = proxy_handler.pop(https)
    return proxy.to_dict if proxy else {"code": 0, "src": "no proxy"}


@app.route('/refresh/')
def refresh():
    # TODO refresh会有守护程序定时执行，由api直接调用性能较差，暂不使用
    return 'success'


@app.route('/all/')
def getAll():
    https = request.args.get("type", "").lower() == 'https'
    proxies = proxy_handler.getAll(https)
    proxies_json = [_.to_dict for _ in proxies]
    #print(type(proxies_json), dir(proxies_json))
    # 按 value 字段倒序排序
    sort_proxies = sorted(proxies_json, key=lambda x: x["check_count"], reverse=True)
    return jsonify(sort_proxies)
    #return jsonify([_.to_dict for _ in proxies])

@app.route('/clear/')
def clear():
    status = proxy_handler.clear()
    return {"code": 0, "src": status}

@app.route('/delete/', methods=['GET'])
def delete():
    proxy = request.args.get('proxy')
    status = proxy_handler.delete(Proxy(proxy))
    return {"code": 0, "src": status}


@app.route('/count/')
def getCount():
    proxies = proxy_handler.getAll()
    http_type_dict = {}
    source_type_dict = {}
    proxy_type_dict = {}
    check_count_dict = {}
    region_count_dict = {}
    avail_proxies_list = [] 

    min_avail_limit = conf.minAvailLimit
    avild_proxies_count = 0
    for proxy in proxies:
        http_type = 'http'
        http_type_dict[http_type] = http_type_dict.get(http_type, 0) + 1
        if proxy.https is True:
            http_type = 'https'
            http_type_dict[http_type] = http_type_dict.get(http_type, 0) + 1
        for source in proxy.source.split('/'):
            source_type_dict[source] = source_type_dict.get(source, 0) + 1
        for proxy_type in re.split(r'[ /、,，]+', proxy.proxy_type):
            proxy_type_dict[proxy_type] = proxy_type_dict.get(proxy_type, 0) + 1
        check_count_dict[f"{(proxy.check_count//min_avail_limit)*min_avail_limit}-{((proxy.check_count//min_avail_limit)+1)*min_avail_limit-1}"] = \
            check_count_dict.get(f"{(proxy.check_count//min_avail_limit)*min_avail_limit}-{((proxy.check_count//min_avail_limit)+1)*min_avail_limit-1}",0) + 1
        if proxy.check_count >= min_avail_limit:
            avail_proxies_list.append(f"{proxy.proxy_type}://{proxy.proxy}")
            avild_proxies_count += 1

        region  = proxy.region.split()[0]
        if region not in region_count_dict:
            region_count_dict[region] = 1
        else:
            region_count_dict[region] += 1


    http_type_sort_dict = OrderedDict(sorted(http_type_dict.items()))
    proxy_type_sort_dict = OrderedDict(sorted(proxy_type_dict.items()))
    source_type_sort_dict = OrderedDict(sorted(source_type_dict.items(), key=lambda x: int(re.search(r'\d+', x[0]).group())))
    check_count_sort_dict = dict(sorted(check_count_dict.items(), key=lambda x: int(x[0].split('-')[0]), reverse=True))
    region_count_sort_dict = dict(sorted(region_count_dict.items(), key=lambda x: x[1], reverse=True))

    #print(check_count_sort_dict)
    return json.dumps(OrderedDict([("count", len(proxies)), ("http_type", http_type_sort_dict), ("proxy_type", proxy_type_sort_dict), 
        ("source", source_type_sort_dict), ("region", region_count_sort_dict),
        ("check_count", check_count_sort_dict), 
        (f"check_count_{min_avail_limit}_count", avild_proxies_count),
        (f"check_count_{min_avail_limit}_proxies", avail_proxies_list)]))
    #return {"http_type": http_type_dict, "source": source_type_dict, "count": len(proxies), "proxy_type": proxy_type_dict, "check_count": check_count_sort_dict}

def runFlask():
    if platform.system() == "Windows":
        app.run(host=conf.serverHost, port=conf.serverPort)
    else:
        import gunicorn.app.base

        class StandaloneApplication(gunicorn.app.base.BaseApplication):

            def __init__(self, app, options=None):
                self.options = options or {}
                self.application = app
                super(StandaloneApplication, self).__init__()

            def load_config(self):
                _config = dict([(key, value) for key, value in iteritems(self.options)
                                if key in self.cfg.settings and value is not None])
                for key, value in iteritems(_config):
                    self.cfg.set(key.lower(), value)

            def load(self):
                return self.application

        _options = {
            'bind': '%s:%s' % (conf.serverHost, conf.serverPort),
            'workers': 4,
            'timeout': 60,
            'keepalive': 0,
            #'accesslog': '-',  # log to stdout
            'accesslog': conf.serverAccessLogFile,
            'errorlog': conf.serverErrorLogFile,
            'access_log_format': '%(h)s %(l)s %(t)s "%(r)s" %(s)s "%(a)s"',
            'daemon': True  # 以 daemon 形式运行
        }
        StandaloneApplication(app, _options).run()


if __name__ == '__main__':
    runFlask()
