#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# 异步的 ORM
#
'''

__author__ = 'whchao'

import logging, asyncio

import aiomysql


def log(sql, args=()):
    logging.info('SQL : %s' % sql)


# 创建连接池， 全局的连接池
async def create_pool(loop, **kw):
    logging.info('create databases connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', '3306'),
        user=kw.get('user', 'root'),
        password=kw.get('password'),
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        loop=loop
    )


async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql.replace("?", '%s'), args or ())
            if size:
                rs = await  cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs

async def execute(sql, args):
    log(sql, args)
    async with __pool.get() as conn:
        try:
            cur = await conn.cursor()
            cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            await cur.close()
            pass
        except BaseException as e:
            raise
        return
