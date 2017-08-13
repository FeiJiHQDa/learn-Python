# coding: utf-8

from collections import Iterator, Iterable

# 切片
L = list(range(10))
print(L)

L1 =  tuple(range(10))
print(L1)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('Setp 3')
    yield(5)

o = odd()

next(o)
next(o)
next(o)

it = iter([1, 2, 4, 5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break