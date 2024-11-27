# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setting.py
   Description :   配置文件
   Author :        007x
   date：          2019/2/15
-------------------------------------------------
   Change Activity:
                   2019/2/15:
-------------------------------------------------
"""

BANNER = r"""
****************************************************************
*** ______  ********************* ______ *********** _  ********
*** | ___ \_ ******************** | ___ \ ********* | | ********
*** | |_/ / \__ __   __  _ __   _ | |_/ /___ * ___  | | ********
*** |  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | | ********
*** | |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___  ****
*** \_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____/ ****
****                       __ / /                          *****
************************* /___ / *******************************
*************************       ********************************
****************************************************************
"""

VERSION = "2.8.0"

# ############### server config ###############
HOST = "0.0.0.0"

PORT = 5010

# ############### database config ###################
# db connection uri
# example:
#      Redis: redis://:password@ip:port/db
#      Ssdb:  ssdb://:password@ip:port
DB_CONN = 'redis://:123456@127.0.0.1:6379/0'

# proxy table name
TABLE_NAME = 'use_proxy'
""" #no usefull
    "freeProxy01",
    "freeProxy02",
    "freeProxy03",
    "freeProxy04",
    "freeProxy05",
    "freeProxy06",
    "freeProxy07",
    "freeProxy08",
    "freeProxy09",
    "freeProxy10",
     
     #usefull
    "freeProxy11",
    "freeProxy12",
    "freeProxy13",
    "freeProxy96"
    "freeProxy97",
    "freeProxy98",
    "freeProxy99",
    "freeProxy100",
    "freeProxy101"
"""
# ###### config the proxy fetch function ######
PROXY_FETCHER = [
    "freeProxy11",
    "freeProxy12",
    "freeProxy13",
    "freeProxy96"
    "freeProxy97",
    "freeProxy98",
    "freeProxy99",
    "freeProxy100",
    "freeProxy101"
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

# ############# proxy attributes #################
# 是否启用代理地域属性
PROXY_REGION = True

SERVER_PIDFILE = '/tmp/proxyPoolServer.pid'
SERVER_ACCESS_LOGFILE =  './log/access.log'
SERVER_ERROR_LOGFILE = './log/error.log'

SCHEDULER_PIDFILE = "/tmp/proxyPoolScheduler.pid"

# ############# scheduler config #################

# Set the timezone for the scheduler forcely (optional)
# If it is running on a VM, and
#   "ValueError: Timezone offset does not match system offset"
#   was raised during scheduling.
# Please uncomment the following line and set a timezone for the scheduler.
# Otherwise it will detect the timezone from the system automatically.

TIMEZONE = "Asia/Shanghai"
