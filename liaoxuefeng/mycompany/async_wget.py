#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s ...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, write = yield from connect