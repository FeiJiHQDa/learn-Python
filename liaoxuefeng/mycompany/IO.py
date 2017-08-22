# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# read All
# try:
#     f = open('ex4.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()


with open('ex4.txt', 'r') as f:
    print(f.read())
    print(f.readline())


import json

d = {'name' : 'wuhcoa', 'bod':75}
c = dict(name=89, age=299, ok=899)
print(json.dumps(d))
print(json.dumps(c))        # 输出双引号
print(c)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))


def A():
    print('1')
    print('2')
    print('3')

def B():
    print('x')
    print('y')
    print('z')

B()
A()

# 消费者
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

# 生产者
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)