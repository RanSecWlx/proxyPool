
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

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;代理IP池项目是从https://github.com/jhao104/proxy_pool.git clone而来，对 ProxyPool 代理的二次魔改，除了原有的HTTP代理外，新增了对SOCKS4、SOCKS5代理协议支持，增加了完善了proxy fetch来源，改善了部分功能，如/count请求、server和schedule模式形成守护进程等，优化修改了部分bug，快速实现大量活跃可用代理的持续监测收集工作。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;代理IP池项目,主要功能为定时采集网上发布或者手工收录的免费代理验证入库，定时验证入库的代理保证代理的可用性，提供API和CLI两种使用方式，同时你也可以扩展代理源以增加代理池IP的质量和数量。</p>

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

### 项目效果

![image](https://github.com/user-attachments/assets/284f6600-d634-433f-b464-c6d175382a36)![image](https://github.com/user-attachments/assets/e9c7de0b-ee25-4aa5-8fb6-4331b16b5631)![image](https://github.com/user-attachments/assets/a178d3b0-2545-4b1e-80aa-74cb557c0f14)
![image](https://github.com/user-attachments/assets/94d97304-8c12-4ed3-8d2d-af57bfc2e875)

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

# getCount时，check_count_xxx_proxies 过滤条件下限，筛选出来质量比较高的代理
MIN_AVAIL_LIMIT = 20

# 解决代理源需fanqiang访问问题
API_PROXY_CONFIG = "http://127.0.0.1:1080"

# 每个proxy采集进程启动的线程数量
RAW_THREADS_NUM = 50

# 每个proxy检查进程启动的线程数量
USE_THREADS_NUM = 10

# proxy采集任务每间隔多少分钟执行一次
RAW_INTERVAL_MIN = 4

# proxy检查任务每间隔多少分钟执行一次
USE_INTERVAL_MIN = 2

# 控制 执行器（如线程池或进程池）中 最大并发执行任务的数量。
THREADPOOL_WORKS_NUM = 60

# 一个进程池（ProcessPoolExecutor），最多可以同时运行多少个进程
PROCESSPOOL_WORKS_NUM = 5

# 控制 同一个任务 在调度器中的最大实例数量
JOB_INSTANCES_NUM = 30

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

    
   2、此外，还可以从网络空间测绘引擎上获取免费代理，比如FOFA引擎： <br>
   &nbsp;&nbsp;&nbsp;&nbsp;获取SOCKS4代理：protocol="socks4" && "Results:request granted";<br>
   &nbsp;&nbsp;&nbsp;&nbsp;获取SOCKS5代理：protocol=="socks5" && "Version:5 Method:No Authentication(0x00)" && after="2022-02-01";<br>
   &nbsp;&nbsp;&nbsp;&nbsp;获取HTTP  代理：server=="Mikrotik HttpProxy" && status_code=="401";<br>


   3、在tmp目录下执行bash run.sh 可以在线获取HTTP、SOCKS4、SOCKS5代理，并自动更新到proxyList目录下的配置文件。<br>

   4、大家可以在tmp目录下run.sh继续完善添加的代理源：<br>
     "HTTP": [<br>
        "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",<br>
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",<br>
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",<br>
        "https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all",<br>
        "https://api.openproxylist.xyz/http.txt",<br>
        "https://multiproxy.org/txt_all/proxy.txt",<br>
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",<br>
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",<br>
        "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",<br>
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",<br>
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",<br>
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",<br>
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",<br>
        "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",<br>
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",<br>
        "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",<br>
        "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",<br>
        "https://rootjazz.com/proxies/proxies.txt",<br>
        "https://spys.me/proxy.txt",<br>
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",<br>
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",<br>
        "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",<br>
        "https://sunny9577.github.io/proxy-scraper/proxies.txt",<br>
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",<br>
        "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",<br>
        "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",<br>
        "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",<br>
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt",
        "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",<br>
        "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",<br>
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",<br>
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",<br>
        "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt",<br>
        "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/refs/heads/main/http.txt",<br>
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/http/data.txt" <br>
      ],<br>
  "SOCKS4": [
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4",<br>
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",<br>
        "https://api.openproxylist.xyz/socks4.txt",<br>
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",<br>
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt",<br>
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",<br>
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",<br>
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",<br>
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",<br>
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",<br>
        "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",<br>
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",<br>
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks4.txt",<br>
        "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt",<br>
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt",<br>
        "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",<br>
        "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt",<br>
        "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt",<br>
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt",<br>
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",<br>
        "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",<br>
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt",<br>
        "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/refs/heads/main/socks4.txt",<br>
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/socks4/data.txt" <br>
      ],<br>
  "SOCKS5": [<br>
        "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",<br>
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",<br>
        "https://api.openproxylist.xyz/socks5.txt",<br>
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",<br>
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",<br>
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",<br>
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",<br>
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",<br>
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",<br>
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",<br>
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt",<br>
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks5.txt",<br>
        "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt",<br>
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",<br>
        "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt",<br>
        "https://spys.me/socks.txt",<br>
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt",<br>
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",<br>
        "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/socks5/global/socks5_checked.txt",<br>
        "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/refs/heads/main/socks5.txt",<br>
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/socks5/data.txt" <br>
      ],<br>
  "HTTPS": [<br>
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",<br>
        "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",<br>
        "https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all",<br>
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt",<br>
        "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt",<br>
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",<br>
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",<br>
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/https/data.txt" <br>
  ]<br>
    
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
    @classmethod
    def freeProxyCustom1(cls):  # 命名不和已有重复即可

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
