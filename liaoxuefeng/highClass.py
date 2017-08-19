# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 枚举类型

from enum import Enum, unique
# from mycompany import test

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name, ' ==> ', ',', member)


# for name, member in Month.__members__.items():
#     print(name, ' ==> ', ',', member)


class Weekday(Enum):
    Sum = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
# print(day1.value)


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value