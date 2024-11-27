# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     launcher
   Description :   启动器
   Author :        007x
   date：          2021/3/26
-------------------------------------------------
   Change Activity:
                   2021/3/26: 启动器
-------------------------------------------------
"""
__author__ = '007x'

import os
import sys
import signal
import daemon
from daemon.pidfile import PIDLockFile
from db.dbClient import DbClient
from handler.logHandler import LogHandler
from handler.configHandler import ConfigHandler

log = LogHandler('launcher')
conf = ConfigHandler()

def startServerProcess():
    __beforeStart()
    from api.proxyApi import runFlask
    with daemon.DaemonContext(
            #stdout=sys.stdout, stderr=sys.stderr,
            working_directory='./',
            pidfile=PIDLockFile(conf.serverPidFile),
            umask=0o022,
            detach_process=True):
        runFlask()
    #runFlask()

def stopServerProcess():
    try:
        with open(conf.serverPidFile, "r") as f:
            pid = int(f.read().strip())
        os.kill(pid, signal.SIGTERM) 
        os.remove(conf.serverPidFile)
        print(f"Server process: {pid} stoped")
        #print("Server pid file removed")
    except FileNotFoundError:
        pass
    except ProcessLookupError:
        pass

def startSchedulerProcess():
    __beforeStart()
    from helper.scheduler import runScheduler
    with daemon.DaemonContext(
            #stdout=sys.stdout, stderr=sys.stderr,
            working_directory='./',
            pidfile=PIDLockFile(conf.schedulerPidFile),
            umask=0o022,
            detach_process=True):
        runScheduler()

def stopSchedulerProcess():
    try:
        with open(conf.schedulerPidFile, "r") as f:
            pid = int(f.read().strip())
        os.kill(pid, signal.SIGTERM)
        os.remove(conf.schedulerPidFile)
        print(f"Server process: {pid} stoped")
        #print("Server pid file removed")
    except FileNotFoundError:
        pass
    except ProcessLookupError:
        pass

def __beforeStart():
    __showVersion()
    __showConfigure()
    if __checkDBConfig():
        log.info('exit!')
        sys.exit()


def __showVersion():
    from setting import VERSION
    log.info("ProxyPool Version: %s" % VERSION)


def __showConfigure():
    log.info("ProxyPool configure HOST: %s" % conf.serverHost)
    log.info("ProxyPool configure PORT: %s" % conf.serverPort)
    log.info("ProxyPool configure PROXY_FETCHER: %s" % conf.fetchers)


def __checkDBConfig():
    db = DbClient(conf.dbConn)
    log.info("============ DATABASE CONFIGURE ================")
    log.info("DB_TYPE: %s" % db.db_type)
    log.info("DB_HOST: %s" % db.db_host)
    log.info("DB_PORT: %s" % db.db_port)
    log.info("DB_NAME: %s" % db.db_name)
    log.info("DB_USER: %s" % db.db_user)
    log.info("=================================================")
    return db.test()
