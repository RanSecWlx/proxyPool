# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     proxy_pool
   Description :   proxy pool 启动入口
   Author :        007x
   date：          2020/6/19
-------------------------------------------------
   Change Activity:
                   2020/6/19:
-------------------------------------------------
"""
__author__ = '007x'

import click
from helper.launcher import startServerProcess, stopServerProcess
from helper.launcher import startSchedulerProcess, stopSchedulerProcess
from setting import BANNER, VERSION

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=VERSION)
def cli():
    """ProxyPool cli工具"""


@cli.command(name="startScheduler")
def startSchedule():
    """ 启动调度程序 """
    click.echo(BANNER)
    startSchedulerProcess()

@cli.command(name="stopScheduler")
def stopSchedule():
    """ 停止调度程序 """
    stopSchedulerProcess()


@cli.command(name="startServer")
def startServer():
    """ 启动api服务 """
    click.echo(BANNER)
    startServerProcess()

@cli.command(name="stopServer")
def stopServer():
    """ 停止api服务 """
    stopServerProcess()

if __name__ == '__main__':
    cli()
