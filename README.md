
ProxyPool 代理IP池
=======

    ______                        ______             _
    | ___ \_                      | ___ \           | |
    | |_/ / \__ __   __  _ __   _ | |_/ /___   ___  | |
    |  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | |
    | |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___
    \_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____\
                           __ / /
                          /___ /

### ProxyPool

代理IP池项目是从https://github.com/jhao104/proxy_pool.git clone而来，对 ProxyPool 代理的二次魔改，除了原有的HTTP代理外，新增了对SOCKS4、SOCKS5代理协议支持，增加了完善了proxy fetch来源，改善了部分功能，如/count请求、server和schedule模式形成守护进程等，优化修改了部分bug，快速实现大量活跃可用代理的持续监测收集工作。代理IP池项目,主要功能为定时采集网上发布或者手工收录的免费代理验证入库，定时验证入库的代理保证代理的可用性，提供API和CLI两种使用方式，同时你也可以扩展代理源以增加代理池IP的质量和数量。

PS:本项目目的：人人可建立属于自己的高质量免费代理池。

* 文档: [document](https://proxy-pool.readthedocs.io/zh/latest/) [![Documentation Status](https://readthedocs.org/projects/proxy-pool/badge/?version=latest)](https://proxy-pool.readthedocs.io/zh/latest/?badge=latest)

* 支持版本: [![](https://img.shields.io/badge/Python-2.7-green.svg)](https://docs.python.org/2.7/)
[![](https://img.shields.io/badge/Python-3.5-blue.svg)](https://docs.python.org/3.5/)
[![](https://img.shields.io/badge/Python-3.6-blue.svg)](https://docs.python.org/3.6/)
[![](https://img.shields.io/badge/Python-3.7-blue.svg)](https://docs.python.org/3.7/)
[![](https://img.shields.io/badge/Python-3.8-blue.svg)](https://docs.python.org/3.8/)
[![](https://img.shields.io/badge/Python-3.9-blue.svg)](https://docs.python.org/3.9/)
[![](https://img.shields.io/badge/Python-3.10-blue.svg)](https://docs.python.org/3.10/)
[![](https://img.shields.io/badge/Python-3.11-blue.svg)](https://docs.python.org/3.11/)

### 运行项目

##### 下载代码:

* git clone

```bash
git clone git@github.com:RanSecWlx/proxyPool.git
```

* releases

```bash
https://github.com/RanSecWlx/proxyPool/releases 下载对应zip文件
```

##### 安装依赖:

```bash
pip install -r requirements.txt
```

##### 更新配置:


```python
# setting.py 为项目配置文件

# 配置API服务

HOST = "0.0.0.0"               # IP
PORT = 5000                    # 监听端口


# 配置数据库

DB_CONN = 'redis://:pwd@127.0.0.1:8888/0'


# 配置 ProxyFetcher

PROXY_FETCHER = [
    "freeProxy01",      # 这里是启用的代理抓取方法名，所有fetch方法位于fetcher/proxyFetcher.py
    "freeProxy02",
    # ....
]

# ############# proxy validator #################
# 代理验证目标网站
HTTP_URL = "http://ifconfig.me/ip"
HTTPS_URL = "https://ifconfig.me/ip"
# 代理验证时超时时间
VERIFY_TIMEOUT = 5

# 近PROXY_CHECK_COUNT次校验中允许的最大失败次数,超过则剔除代理
MAX_FAIL_COUNT = 0

# 近PROXY_CHECK_COUNT次校验中允许的最大失败率,超过则剔除代理
MAX_FAIL_RATE = 0.3

# proxyCheck时代理数量少于POOL_SIZE_MIN触发抓取
POOL_SIZE_MIN = 2000

# getAll时，check_count_xxx_proxies 过滤条件下限，筛选出来质量比较高的代理
MIN_AVAIL_LIMIT = 20

```

#### 免费代理源

   1、目前实现的采集免费代理网站有(排名不分先后, 下面仅是对其发布的免费代理情况, 付费代理测评可以参考[这里](https://zhuanlan.zhihu.com/p/33576641)): 
   
    https://github.com/proxifly/free-proxy-list
    https://github.com/TheSpeed/SOCKS-List
    https://github.com/monosans/proxy-list
    https://proxy5.net
    https://api.openproxylist.xyz/
    https://fineproxy.org/
    https://api.proxyscrape.com/
    https://www.freeproxy.world/
    https://proxyelite.info
    https://geoxy.io/
    https://proxylist.geonode.com

    
   2、此外，还可以从网络空间测绘引擎上获取免费代理，比如FOFA引擎： 
    获取SOCKS4代理：protocol="socks4" && "Results:request granted";
    获取SOCKS5代理：protocol=="socks5" && "Version:5 Method:No Authentication(0x00)" && after="2022-02-01";
    获取HTTP  代理：server=="Mikrotik HttpProxy" && status_code=="401";


   3、在tmp目录下执行bash run.sh 可以在线获取HTTP、SOCKS4、SOCKS5代理，并自动更新到proxyList目录下的配置文件。

    
  如果还有其他好的免费代理网站, 可以在提交在[issues](https://github.com/RanSecWlx/proxyPool/issues/), 下次更新时会考虑在项目中支持。


#### 启动项目:

```bash
# 如果已经具备运行条件, 可用通过proxyPool.py启动。
# 程序分为: schedule 调度程序 和 server Api服务
python3 proxyPool.py 
Usage: proxyPool.py [OPTIONS] COMMAND [ARGS]...

  ProxyPool cli工具

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  startScheduler  启动调度程序
  startServer     启动api服务
  stopScheduler   停止调度程序
  stopServer      停止api服务

# 启停调度程序
python3 proxyPool.py startSchedule
python3 proxyPool.py stopSchedule

# 启停webApi服务
python3 proxyPool.py startServer
python3 proxyPool.py stopServer
```

### 使用
![1732693761872](https://github.com/user-attachments/assets/2d9ae32c-0efe-4113-b1b0-c55b385c5c96)

* Api

启动web服务后, 默认配置下会开启 http://127.0.0.1:5010 的api接口服务:

| api | method | Description | params|
| ----| ---- | ---- | ----|
| / | GET | api介绍 | None |
| /get | GET | 随机获取一个代理| 可选参数: `?type=https` 过滤支持https的代理|
| /pop | GET | 获取并删除一个代理| 可选参数: `?type=https` 过滤支持https的代理|
| /all | GET | 获取所有代理 |可选参数: `?type=https` 过滤支持https的代理|
| /count | GET | 查看代理数量 |None|
| /delete | GET | 删除代理  |`?proxy=host:ip`|
| /clear | GET | 清空代理  |None|

* 爬虫使用

　　如果要在爬虫代码中使用的话， 可以将此api封装成函数直接使用，例如：

```python
import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code

def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy().get("proxy")
    while retry_count > 0:
        try:
            html = requests.get('http://www.example.com', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 删除代理池中代理
    delete_proxy(proxy)
    return None
```

### 扩展代理

　　项目默认包含几个免费的代理获取源，但是免费的毕竟质量有限，所以如果直接运行可能拿到的代理质量不理想。所以，提供了代理获取的扩展方法。

　　添加一个新的代理源方法如下:

* 1、首先在[ProxyFetcher](https://github.com/RanSecWlx/proxyPool/blob/1a3666283806a22ef287fba1a8efab7b94e94bac/fetcher/proxyFetcher.py#L21)类中添加自定义的获取代理的静态方法，
该方法需要以生成器(yield)形式返回`host:ip`格式的代理，例如:

```python

class ProxyFetcher(object):
    # ....

    # 自定义代理源获取方法
    @staticmethod
    def freeProxyCustom1():  # 命名不和已有重复即可

        # 通过某网站或者某接口或某数据库获取代理
        # 假设你已经拿到了一个代理列表
        proxies = ["x.x.x.x:3128", "x.x.x.x:80"]
        for proxy in proxies:
            yield proxy
        # 确保每个proxy都是 host:ip正确的格式返回
```

* 2、添加好方法后，修改[setting.py](https://github.com/RanSecWlx/proxyPool/blob/1a3666283806a22ef287fba1a8efab7b94e94bac/setting.py#L47)文件中的`PROXY_FETCHER`项：

　　在`PROXY_FETCHER`下添加自定义方法的名字:

```python
PROXY_FETCHER = [
    "freeProxy01",    
    "freeProxy02",
    # ....
    "freeProxyCustom1"  #  # 确保名字和你添加方法名字一致
]
```


　　`schedule` 进程会每隔一段时间抓取一次代理，下次抓取时会自动识别调用你定义的方法。


### 问题反馈

　　任何问题欢迎在[Issues](https://github.com/RanSecWlx/proxyPool/issues) 中反馈。

　　你的反馈会让此项目变得更加完美。

### 贡献代码

　　这里感谢以下contributor的无私奉献：

　[@jhao104](https://github.com/jhao104) |　[@kangnwh](https://github.com/kangnwh) | [@bobobo80](https://github.com/bobobo80) | [@halleywj](https://github.com/halleywj) | [@newlyedward](https://github.com/newlyedward) | [@wang-ye](https://github.com/wang-ye) | [@gladmo](https://github.com/gladmo) | [@bernieyangmh](https://github.com/bernieyangmh) | [@PythonYXY](https://github.com/PythonYXY) | [@zuijiawoniu](https://github.com/zuijiawoniu) | [@netAir](https://github.com/netAir) | [@scil](https://github.com/scil) | [@tangrela](https://github.com/tangrela) | [@highroom](https://github.com/highroom) | [@luocaodan](https://github.com/luocaodan) | [@vc5](https://github.com/vc5) | [@1again](https://github.com/1again) | [@obaiyan](https://github.com/obaiyan) | [@zsbh](https://github.com/zsbh) | [@jiannanya](https://github.com/jiannanya) | [@Jerry12228](https://github.com/Jerry12228)  


### Release Notes

   [changelog](https://github.com/RanSecWlx/proxyPool/blob/master/docs/changelog.rst)
