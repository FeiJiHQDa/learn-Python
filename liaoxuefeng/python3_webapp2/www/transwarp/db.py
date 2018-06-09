#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'wuhaichao'

'''
Database operation module.
'''


import time, uuid, functools, threading, logging

#dict object:

class _Engine(object):
    def __init__(self, connect):
        self._connect = connect
    def connect(self):
        return self._connect