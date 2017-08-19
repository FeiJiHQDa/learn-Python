from liaoxuefeng.mycompany.two import *
from liaoxuefeng.mycompany.hello import *
import logging
logging.basicConfig(level=logging.INFO)
print(a)
print( b)

try:
    print('try...')
    r = 10 / 0
    print('return:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

test()

s = '0'
n = int(s)
logging.info('n = %d' % n)