# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test.py  
   Description :  
   Author :       007x
   date：          2017/3/7
-------------------------------------------------
   Change Activity:
                   2017/3/7: 
-------------------------------------------------
"""
__author__ = '007x'

from test import testProxyValidator
from test import testConfigHandler
from test import testLogHandler
from test import testDbClient

if __name__ == '__main__':
    print("ConfigHandler:")
    testConfigHandler.testConfig()

    print("LogHandler:")
    testLogHandler.testLogHandler()

    print("DbClient:")
    testDbClient.testDbClient()

    print("ProxyValidator:")
    testProxyValidator.testProxyValidator()
