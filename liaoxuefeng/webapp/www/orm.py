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
        host=kw.get('host', '127.0.0.1'),
        port=kw.get('port', 3306),
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

# 支持 insert update delete，
async def execute(sql, args, autocommit=True):
    log(sql)
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected

def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)

# 元类  将具体的子类如User的映射信息读取出来
class ModelMetaclass(type):
    pass

# Model  模型
class Model(dict, metaclass=ModelMetaclass):
    pass