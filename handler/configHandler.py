# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     configHandler
   Description :
   Author :        007x
   date：          2020/6/22
-------------------------------------------------
   Change Activity:
                   2020/6/22:
-------------------------------------------------
"""
__author__ = '007x'

import os
import setting
from util.singleton import Singleton
from util.lazyProperty import LazyProperty
from util.six import reload_six, withMetaclass


class ConfigHandler(withMetaclass(Singleton)):

    def __init__(self):
        pass

    @LazyProperty
    def serverHost(self):
        return os.environ.get("HOST", setting.HOST)

    @LazyProperty
    def serverPort(self):
        return os.environ.get("PORT", setting.PORT)

    @LazyProperty
    def dbConn(self):
        return os.getenv("DB_CONN", setting.DB_CONN)

    @LazyProperty
    def tableName(self):
        return os.getenv("TABLE_NAME", setting.TABLE_NAME)

    @property
    def fetchers(self):
        reload_six(setting)
        return setting.PROXY_FETCHER

    @LazyProperty
    def httpUrl(self):
        return os.getenv("HTTP_URL", setting.HTTP_URL)

    @LazyProperty
    def httpsUrl(self):
        return os.getenv("HTTPS_URL", setting.HTTPS_URL)

    @LazyProperty
    def serverPidFile(self):
        return os.getenv("SERVER_PIDFILE", setting.SERVER_PIDFILE)

    @LazyProperty
    def serverAccessLogFile(self):
        return os.getenv("SERVER_ACCESS_LOGFILE", setting.SERVER_ACCESS_LOGFILE)
    
    @LazyProperty
    def serverErrorLogFile(self):
        return os.getenv("SERVER_ERROR_LOGFILE", setting.SERVER_ERROR_LOGFILE)
    
    @LazyProperty
    def schedulerPidFile(self):
        return os.getenv("SCHEDULER_PIDFILE", setting.SCHEDULER_PIDFILE)
    
    @LazyProperty
    def verifyTimeout(self):
        return int(os.getenv("VERIFY_TIMEOUT", setting.VERIFY_TIMEOUT))

    @LazyProperty
    def proxyCheckCount(self):
        return int(os.getenv("PROXY_CHECK_COUNT", setting.PROXY_CHECK_COUNT))

    @LazyProperty
    def maxFailCount(self):
        return int(os.getenv("MAX_FAIL_COUNT", setting.MAX_FAIL_COUNT))

    @LazyProperty
    def maxFailRate(self):
        return float(os.getenv("MAX_FAIL_RATE", setting.MAX_FAIL_RATE))

    @LazyProperty
    def minAvailLimit(self):
        return int(os.getenv("MIN_AVAIL_LIMIT", setting.MIN_AVAIL_LIMIT))

    @LazyProperty
    def poolSizeMin(self):
        return int(os.getenv("POOL_SIZE_MIN", setting.POOL_SIZE_MIN))

    @LazyProperty
    def proxyRegion(self):
        return bool(os.getenv("PROXY_REGION", setting.PROXY_REGION))

    @LazyProperty
    def apiProxyConfig(self):
        return os.getenv("API_PROXY_CONFIG", setting.API_PROXY_CONFIG)

    @LazyProperty
    def rawThreadsNum(self):
        return os.getenv("RAW_THREADS_NUM", setting.RAW_THREADS_NUM)

    @LazyProperty
    def useThreadsNum(self):
        return os.getenv("USE_THREADS_NUM", setting.USE_THREADS_NUM)
    
    @LazyProperty
    def rawIntervalMin(self):
        return os.getenv("RAW_INTERVAL_MIN", setting.RAW_INTERVAL_MIN)

    @LazyProperty
    def useIntervalMin(self):
        return os.getenv("USE_INTERVAL_MIN", setting.USE_INTERVAL_MIN)

    @LazyProperty
    def threadPoolWorksNum(self):
        return os.getenv("THREADPOOL_WORKS_NUM", setting.THREADPOOL_WORKS_NUM)

    @LazyProperty
    def processPoolWorksNum(self):
        return os.getenv("PROCESSPOOL_WORKS_NUM", setting.PROCESSPOOL_WORKS_NUM)

    @LazyProperty
    def jobInstancesNum(self):
        return os.getenv("JOB_INSTANCES_NUM", setting.JOB_INSTANCES_NUM)

    @LazyProperty
    def timezone(self):
        return os.getenv("TIMEZONE", setting.TIMEZONE)

