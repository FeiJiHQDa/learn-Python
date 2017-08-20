#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# 异步的 ORM
#
'''

__author__  ='whchao'

import logging, asyncio

import aiomysql

def log(sql, args=()):
    logging.info('SQL : %s' % sql)

async def create_pool(loop, **kw):
    logging.info('create databases connection pool...')
    global __pool
    __pool = await aiomysql.create_pool
